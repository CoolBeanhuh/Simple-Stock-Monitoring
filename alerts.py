def evaluate_alerts(symbol, close, previous_close, rules):
    """Return messages for rules satisfied by the most recent daily close."""
    if previous_close <= 0:
        raise ValueError("Previous close must be positive")
    change_pct = (close / previous_close - 1) * 100
    messages = []
    if "below" in rules and close < rules["below"]:
        messages.append(f"{symbol}: close {close:.2f} below {rules['below']:.2f}")
    if "above" in rules and close > rules["above"]:
        messages.append(f"{symbol}: close {close:.2f} above {rules['above']:.2f}")
    if "daily_drop_pct" in rules and change_pct <= -rules["daily_drop_pct"]:
        messages.append(f"{symbol}: down {abs(change_pct):.2f}% today (close {close:.2f})")
    if "daily_rise_pct" in rules and change_pct >= rules["daily_rise_pct"]:
        messages.append(f"{symbol}: up {change_pct:.2f}% today (close {close:.2f})")
    return messages
