import json
import logging
from pathlib import Path
from zoneinfo import ZoneInfo
from datetime import datetime

from src.alerts import evaluate_alerts
from src.market_data import latest_closes
from src.notifications import send_telegram

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def run():
    config = json.loads(Path("config.json").read_text(encoding="utf-8"))
    today_ny = datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    messages = []
    failures = []
    for symbol, rules in config["stocks"].items():
        try:
            session_date, close, previous_close = latest_closes(symbol)
            if session_date != today_ny:
                logging.info("Skipping %s: latest session %s is not today", symbol, session_date)
                continue
            messages.extend(evaluate_alerts(symbol, close, previous_close, rules))
        except Exception as exc:
            logging.exception("Could not process %s", symbol)
            failures.append(f"{symbol}: {type(exc).__name__}")
    if messages:
        send_telegram("StockWatch alerts — " + today_ny + "\n" + "\n".join(messages))
        logging.info("Sent %d alerts", len(messages))
    else:
        logging.info("No alerts today")
    if failures:
        raise RuntimeError("Failed symbols: " + ", ".join(failures))


if __name__ == "__main__":
    run()
