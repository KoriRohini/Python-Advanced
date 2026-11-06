class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}, {self.balance}"

    def __add__(self, other):
        return Account("combined",
                       self.balance + other.balance)

a1 = Account("navin", 1000)
a2 = Account("kiran", 2000)

combined = a1 + a2

print(a1)
print(a2)
print(combined)