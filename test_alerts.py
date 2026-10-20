import unittest
from src.alerts import evaluate_alerts


class AlertTests(unittest.TestCase):
    def test_drop(self):
        self.assertEqual(len(evaluate_alerts("TEST", 90, 100, {"daily_drop_pct": 5})), 1)

    def test_no_alert(self):
        self.assertEqual(evaluate_alerts("TEST", 99, 100, {"daily_drop_pct": 5}), [])

    def test_below(self):
        self.assertEqual(len(evaluate_alerts("TEST", 90, 100, {"below": 95})), 1)


if __name__ == "__main__":
    unittest.main()
