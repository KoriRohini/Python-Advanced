class Laptop:
    def build(self):
        print("Laptop Building Projects")

class Desktop:
    def build(self):
        print("Desktop Building Projects")

class Alien:
    def code(self, machine):
        print("Development started")
        machine.build()

Alien().code(Laptop())
Alien().code(Desktop())
