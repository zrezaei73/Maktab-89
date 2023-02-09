import unittest
import bank_account
import re


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Customer('Akbar', 'Babaii', '09123456789', 'akbar@gmail.com')
        self.p2 = Customer('Asqar', 'Rezaii', '09123456788', 'asqar@gmail.com')

    def tearDown(self):
        print('Done!')

    def test_full_name(self):
        self.assertEqual(self.p1.full_name(), 'Akbar Babaii')
        self.assertEqual(self.p2.full_name(), 'Asqar Rezaii')

     # def test_phone(self):
        # phone_pattern = r'^((\+98|0)9\d{9})$'
        # with self.assertRaises(ValueError):
    # def test_email(self):
    #     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #     with self.assertRaises(ValueError):

class BankAccountTests(unittest.TestCase):
    def setUp(self):
        WAGE_AMOUNT = 600  # کارمزد
        MIN_BALANCE = 10000
        self.p1 = BankAccount('Akbar', 100000)
        self.p2 = BankAccount('Asqar', 200000)
        self.account = BankAccount()

    def test__check_minimum_balance(self):
        self.assertGreater(self.p1.__check_minimum_balance(100000), self.MIN_BALANCE)
        self.assertGreater(self.p2.__check_minimum_balance(200000), self.MIN_BALANCE)

    def test_set_owner(self):
        self.assertNotEqual(self.p1.full_name, self.p2.full_name)

    def test_get_owner(self):
        self.assertEqual(self.p1.get_owner(), self.p1.get_owner())

    def test_withdraw(self):
        p1.deposite(100)
        outcome = p1.withdraw(10000)
        self.assertFalse(outcome)

    def test_deposit(self):
        p1.deposit(1000)
        p1.__balance += 1000
        self.assertEqual(self.p1.__balance, 101000)

    def test_get_balance(self):
        pass

    def test_transfer(self):
       pass

    def test_change_wage(cls):
        cls.assertGreater(cls.bankaccount.change_wage.WAGE_AMOUNT, 0)
    def test_change_min_balance(cls):
        cls.assertGreater(cls.bankaccount.change_min_balance.MIN_BALANCE, 0)

    def test_account_balance_is_zero_after_it_was_created(self):
        self.assertEqual(account.get_balance(), 0)
    def test_account_balance_after_thousands_dollars_was_given(self):
        account.deposit(1000)
        seld.assertEqual(account.get_balance(), 1000)
    def test_when_negative_number_is_given_valueError_is_thrown(self):
        # self.assertRaises(ValueError,  account.deposit(), -1000)
        with self.assertRaises(ValueError):
            account.deposit(-1000)






    # def test_legal_withdraw(self):
    #     self.test.BankAccount.MinBalanceError.withdraw_amount >= 10000
    #     self.assertLessEqual(10000, self.account.__balance, 'insufficient balance')
    #
    # def test_get_balance(self):
    #     self.assertEqual(10000 + self.account.WAGE_AMOUNT, _BankAccount__Balance, 'insufficient balance')
    #
    # def test_transfer(self):
    #     self.account.transfer(self.account, 1000)
    #     self.assertLessEqual(10000, self.account.__balance, 'insufficient balance')

if __name__ == '__main__':
    unittest.main()







