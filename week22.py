# class Car:
#     def __init__(self, make_in, model_in, cc_in):
#         self.make = make_in
#         self.model = model_in
#         self.cc = cc_in
#     def print(self):
#         print("Make ", self.make)
#         print("Model ", self.model)
#         print("CC ", self.cc)
# class RaceCar(Car):
#     def __init__(self):
#         super().__init__("Honda", "Civic", 1600)
#         self.races_won = 0
#     def print(self):
#         super().print()
#         print("Races Won", self.races_won)
# r1 = RaceCar()
# r1.print()

# class Car:
#     def __init__(self, make_in, model_in, cc_in):
#         self.make = make_in
#         self.model = model_in
#         self.cc = cc_in
#     def print(self):
#         print("Make ", self.make)
#         print("Model ", self.model)
#         print("CC ", self.cc)
# class RaceCar(Car):
#     def __init__(self, make_in, model_in, cc_in, race_won_in):
#         super().__init__(make_in, model_in, cc_in)
#         self.races_won = race_won_in
#     def print(self):
#         super().print()
#         print("Races Won", self.races_won)
# rc1 = RaceCar("Audi", "RS", 2890, 2)
# rc1.print()

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def get_balance(self):
#         return self.balance
# class SavingsAccount(BankAccount):
#     def __init__(self, interest_rate_in):
#         super().__init__()
#         self.interest_rate = interest_rate_in
#     def add_interest(self):
#         interest = self.get_balance() * (self.interest_rate / 100)
#         self.deposit(interest)
# sa1 = SavingsAccount(10)
# sa1.deposit(100)
# sa1.add_interest()
# print("Balance: €" + str(sa1.get_balance()))

