import unittest
import uuid
import datetime
import hashlib
from main import *

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        user = "John Doe"
        ba = BankAccount(user)
        ba.deposit(100)
        self.assertEqual(ba.balance, 100)

    def test_withdraw(self):
        user = "John Doe"
        ba = BankAccount(user, balance=100)
        ba.withdraw(50)
        self.assertEqual(ba.balance, 50)

    def test_withdraw_exception(self):
        user = "John Doe"
        ba = BankAccount(user, balance=100)
        with self.assertRaises(Exception) as context:
            ba.withdraw(150)
        self.assertEqual(str(context.exception), "Insufficient balance.")

class TestPassenger(unittest.TestCase):
    def test_generate_id(self):
        name = "John Doe"
        p = Passenger(name, BankAccount(name))
        id = hashlib.sha256(str(datetime.datetime.now().timestamp()).encode()).hexdigest()
        self.assertEqual(p.generate_id(), id)

    def test_create_passenger(self):
        name = "John Doe"
        p = Passenger.create_passenger(name)
        self.assertEqual(p.name, name)
        self.assertIsInstance(p.bank_account, BankAccount)

class TestMetroCard(unittest.TestCase):
    def test_charge(self):
        user = "John Doe"
        mc = MetroCard(user)
        mc.charge(100)
        self.assertEqual(mc.balance, 100)

    def test_deduct(self):
        user = "John Doe"
        mc = MetroCard(user, balance=100)
        mc.deduct(50)
        self.assertEqual(mc.balance, 50)

class TestSingleTable(unittest.TestCase):
    def test_use_successful(self):
        user = "Test User"
        single_table = SingleTable(user)
        fare = 10
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        trip = single_table.use(fare, start_time, end_time)
        self.assertIsInstance(trip, Trip)
        self.assertEqual(trip.fare, fare)
        self.assertEqual(trip.start_time, start_time)
        self.assertEqual(trip.end_time, end_time)
        self.assertTrue(trip.is_active)

    def test_use_failed(self):
        user = "Test User"
        single_table = SingleTable(user)
        fare = 10
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        single_table.use(fare, start_time, end_time)
        with self.assertRaises(Exception) as context:
            single_table.use(fare, start_time, end_time)
        self.assertEqual(str(context.exception), "This card has already been used.")

class TestCredit(unittest.TestCase):
    def test_use_successful(self):
        user = "Test User"
        credit = Credit(user)
        credit.charge(100)
        fare = 10
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        trip = credit.use(fare, start_time, end_time)
        self.assertIsInstance(trip, Trip)
        self.assertEqual(trip.fare, fare)
        self.assertEqual(trip.start_time, start_time)
        self.assertEqual(trip.end_time, end_time)
        self.assertEqual(credit.balance, 90)

    def test_use_failed(self):
        user = "Test User"
        credit = Credit(user)
        fare = 10
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        with self.assertRaises(Exception) as context:
            credit.use(fare, start_time, end_time)
        self.assertEqual(str(context.exception), "Insufficient balance.")

class TestCredit(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe", "johndoe@email.com")
        self.credit = Credit(self.user)
        self.credit.add_balance(100)
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    
    def test_use(self):
        trip = self.credit.use(10, self.start_time, self.end_time)
        self.assertIsInstance(trip, Trip)
        self.assertEqual(trip.fare, 10)
        self.assertEqual(trip.start_time, self.start_time)
        self.assertEqual(trip.end_time, self.end_time)
        self.assertEqual(self.credit.balance, 90)

        with self.assertRaises(Exception) as context:
            self.credit.use(100, self.start_time, self.end_time)
        self.assertEqual(str(context.exception), "Insufficient balance.")

class TestTerm(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe", "johndoe@email.com")
        expiry_date = datetime.datetime.now().date() + datetime.timedelta(days=365)
        self.term = Term(self.user, expiry_date)
        self.term.add_balance(100)
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now() + datetime.timedelta(hours=1)

if __name__ == '__main__':
    unittest.main()
# def test_use(self):
#     trip = self.term.use(10, self.start_time, self.end_time)
#     self.assertIsInstance(trip, Trip)




# class TestUser(unittest.TestCase):
# def setUp(self):
# self.user = User("John Doe", "johndoe@email.com", "password")
#
# def test_user_registration(self):
#     self.assertEqual(self.user.name, "John Doe")
#     self.assertEqual(self.user.email, "johndoe@email.com")
#     self.assertEqual(self.user.password, "password")
#     self.assertEqual(self.user.balance, 0)
#
# def test_deposit(self):
#     self.user.deposit(100)
#     self.assertEqual(self.user.balance, 100)
#
# def test_withdraw(self):
#     self.user.deposit(100)
#     self.user.withdraw(50)
#     self.assertEqual(self.user.balance, 50)
#
# def test_insufficient_balance(self):
#     self.user.deposit(100)
#     self.user.withdraw(150)
#     self.assertEqual(self.user.balance, 100)
#
# class TestMetroTrip(unittest.TestCase):
# def setUp(self):
# self.trip = MetroTrip(1, 1, "Standard", "Online", 50)
# def test_trip_registration(self):
#     self.assertEqual(self.trip.trip_id, 1)
#     self.assertEqual(self.trip.user_id, 1)
#     self.assertEqual(self.trip.metro_card_type, "Standard")
#     self.assertEqual(self.trip.order_registration, "Online")
#     self.assertEqual(self.trip.fee, 50)
#
# class TestAdmin(unittest.TestCase):
# def setUp(self):
# self.admin = Admin("admin", "password")
# self.trip = MetroTrip(1, 1, "Standard", "Online", 50)
# def test_register_trip(self):
#     registered_trip = self.admin.register_trip(2, 2, "Standard", "Online", 60)
#     self.assertEqual(registered_trip.trip_id, 2)
#     self.assertEqual(registered_trip.user_id, 2)
#     self.assertEqual(registered_trip.metro_card_type, "Standard")
#     self.assertEqual(registered_trip.order_registration, "Online")
#     self.assertEqual(registered_trip.fee, 60)
#
# def test_edit_trip(self):
#     self.admin.edit_trip(self.trip, 70)
#     self.assertEqual(self.trip.fee, 70)
#
# def test_delete_trip(self):
#     self.admin.delete_trip(self.trip)
#
# if name == 'main':
# unittest.main()



# import unittest
# import pickle
# import datetime
# import hashlib
# import uuid
#
# class TestBankAccount(unittest.TestCase):
#     def test_bank_account(self):
#         user = "John Doe"
#         ba = BankAccount(user)
#         self.assertEqual(ba.user, user)
#         self.assertEqual(ba.balance, 0)
#
#         ba.deposit(100)
#         self.assertEqual(ba.balance, 100)
#
#         try:
#             ba.withdraw(200)
#         except Exception as e:
#             self.assertEqual(str(e), "Insufficient balance.")
#
#         self.assertEqual(ba.balance, 100)
#         ba.withdraw(50)
#         self.assertEqual(ba.balance, 50)
#
# class TestPassenger(unittest.TestCase):
#     def test_passenger(self):
#         name = "John Doe"
#         ba = BankAccount(name)
#         passenger = Passenger(name, ba)
#         self.assertEqual(passenger.name, name)
#         self.assertIsInstance(passenger.bank_account, BankAccount)
#         self.assertIsNotNone(passenger.id)
#
#         passenger_id = passenger.id
#         self.assertEqual(passenger.generate_id(), passenger_id)
#
#         with open("users.pickle", "wb") as f:
#             pickle.dump(passenger, f)
#
#         with open("users.pickle", "rb") as f:
#             passenger_from_file = pickle.load(f)
#         self.assertEqual(passenger_from_file.id, passenger_id)
#         self.assertEqual(passenger_from_file.name, name)
#         self.assertIsInstance(passenger_from_file.bank_account, BankAccount)
#
#         passenger_2 = Passenger.create_passenger("Jane Doe")
#         self.assertEqual(passenger_2.name, "Jane Doe")
#         self.assertIsInstance(passenger_2.bank_account, BankAccount)
#         self.assertIsNotNone(passenger_2.id)
#
#         with open("users.pickle", "rb") as f:
#             passenger_2_from_file = pickle.load(f)
#         self.assertEqual(passenger_2_from_file.id, passenger_2.id)
#         self.assertEqual(passenger_2_from_file.name, "Jane Doe")
#         self.assertIsInstance(passenger_2_from_file.bank_account, BankAccount)
#
# class TestMetroCard(unittest.TestCase):
#     def test_charge(self):
#         user = "John Doe"
#         metro_card = MetroCard(user)
#         metro_card.charge(100)
#         self.assertEqual(metro_card.balance, 100)
#
#     def test_deduct(self):
#         user = "Jane Doe"
#         metro_card = MetroCard(user, 200)
#         metro_card.deduct(100)
#         self.assertEqual(metro_card.balance, 100)
#
# class TestSingleTable(unittest.TestCase):
#     def test_use(self):
#         user = "John Doe"
#         single_table = SingleTable(user)
#         fare = 100
#         start_time = datetime.datetime.now()
#         end_time = start_time + datetime.timedelta(hours=1)
#         trip = single_table.use(fare, start_time, end_time)
#         self.assertIsInstance(trip, Trip)
#         self.assertEqual(trip.fare, fare)
#         self.assertEqual(trip.start_time, start_time)
#         self.assertEqual(trip.end_time, end_time)
#         self.assertTrue(trip.is_active)
#
#     def test_use_already_used(self):
#         user = "John Doe"
#         single_table = SingleTable(user)
#         single_table.use(100, datetime.datetime.now(), datetime.datetime.now())
#         with self.assertRaises(Exception) as context:
#             single_table.use(100, datetime.datetime.now(), datetime.datetime.now())
#         self.assertEqual(str(context.exception), "This card has already been used.")


