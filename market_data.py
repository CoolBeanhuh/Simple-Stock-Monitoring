import pandas as pd
import yfinance as yf


def latest_closes(symbol):
    """Return (session date, close, previous close) from completed daily bars."""
    data = yf.Ticker(symbol).history(period="10d", interval="1d", auto_adjust=True)
    closes = data["Close"].dropna()
    if len(closes) < 2:
        raise ValueError(f"Not enough daily data for {symbol}")
    date = pd.Timestamp(closes.index[-1]).date().isoformat()
    return date, float(closes.iloc[-1]), float(closes.iloc[-2])
