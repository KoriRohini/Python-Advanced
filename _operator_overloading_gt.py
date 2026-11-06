class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __gt__(self, other):
        return self.balance > other.balance

navin = Account("navin", 4000)
kiran = Account("kiran", 2000)

if navin > kiran:
    print("navin pays the bill")
else:
    print("kiran pays the bill")