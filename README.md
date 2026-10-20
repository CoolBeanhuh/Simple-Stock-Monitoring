# StockWatch — Daily Stock Alerts

Personal Python project that checks US/Canadian stock closing prices and sends Telegram alerts when configurable thresholds are met.

## Features
- Price above/below thresholds
- Daily percentage rise/drop thresholds
- Weekday scheduled execution using GitHub Actions
- Telegram notifications
- Unit tests for alert logic

## Setup
1. Install Python 3.12, then run `pip install -r requirements.txt`.
2. Edit `config.json` to choose symbols and rules. `.TO` suffix denotes Toronto listings.
3. In Telegram, talk to `@BotFather`, use `/newbot`, and save the bot token privately.
4. Send a message to your bot. Visit `https://api.telegram.org/bot<TOKEN>/getUpdates` privately to find your chat ID.
5. In GitHub repository Settings → Secrets and variables → Actions, add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
6. Enable Actions and run **Daily stock check** using **Run workflow** to test. Normal weekday runs occur at 22:30 UTC.
7. Locally, set those two environment variables and run `python -m src.main`.

## Important limitations
- `yfinance` is a prototyping data source, not a guaranteed real-time market feed.
- The workflow uses a fixed UTC schedule, so it runs at 5:30 PM EST in winter and 6:30 PM EDT in summer. GitHub schedules can be delayed or skipped.
- The program only evaluates a bar if its date matches the current New York date, avoiding alerts from prior trading days on holidays.
- **No durable alert deduplication:** rerunning the workflow on the same trading day can resend the same alert. A future release should add persistent alert state.
- Prices are adjusted daily closing prices, not necessarily raw execution prices.
- The project is for personal research, not investment advice.
- Never commit API tokens, chat IDs, or financial account information.

## Run tests
`python -m unittest discover -s tests`
