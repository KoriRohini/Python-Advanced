class Laptop:

    def build(self):
        print("Laptop Building Projects")

class Alien:

    def code(self, machine):
        print("Development started")
        machine.build()

asus = Laptop()

navin = Alien()
navin.code(asus)