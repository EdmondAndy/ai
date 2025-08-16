import unittest

# Assume this is from accounts import Account, get_share_price
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def test_initialization(self):
        account = Account(account_id=1, initial_deposit=1000.0)
        self.assertEqual(account.account_id, 1)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account.get_holdings(), {})
        self.assertEqual(account.get_transaction_history(), [])

    def test_deposit(self):
        account = Account(account_id=2, initial_deposit=500.0)
        self.assertTrue(account.deposit(500.0))
        self.assertEqual(account.balance, 1000.0)
        self.assertFalse(account.deposit(-100.0))
        self.assertEqual(account.balance, 1000.0)

    def test_withdraw(self):
        account = Account(account_id=3, initial_deposit=500.0)
        self.assertTrue(account.withdraw(400.0))
        self.assertEqual(account.balance, 100.0)
        self.assertFalse(account.withdraw(200.0))
        self.assertEqual(account.balance, 100.0)

    def test_buy_shares(self):
        account = Account(account_id=4, initial_deposit=1000.0)
        self.assertTrue(account.buy_shares('AAPL', 5))
        self.assertEqual(account.balance, 250.0)
        self.assertEqual(account.get_holdings(), {'AAPL': 5})
        self.assertFalse(account.buy_shares('AAPL', 10))
        self.assertEqual(account.balance, 250.0)
        self.assertEqual(account.get_holdings(), {'AAPL': 5})
        
    def test_sell_shares(self):
        account = Account(account_id=5, initial_deposit=1500.0)
        account.buy_shares('TSLA', 2)
        self.assertTrue(account.sell_shares('TSLA', 1))
        self.assertEqual(account.balance, 1150.0)
        self.assertEqual(account.get_holdings(), {'TSLA': 1})
        self.assertFalse(account.sell_shares('TSLA', 2))
        
    def test_portfolio_value(self):
        account = Account(account_id=6, initial_deposit=100.0)
        account.buy_shares('GOOGL', 1)
        self.assertEqual(account.calculate_portfolio_value(), 2900.0)

    def test_profit_or_loss(self):
        account = Account(account_id=7, initial_deposit=3000.0)
        account.buy_shares('GOOGL', 1)
        self.assertEqual(account.calculate_profit_or_loss(), -200.0)

if __name__ == '__main__':
    unittest.main()