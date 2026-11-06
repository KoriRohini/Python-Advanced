class Computer:

    def __init__(self):
        print("init called")
        self.cpu = "i5"

com = Computer()
com1 = Computer()

print(com.cpu)
print(com1.cpu)