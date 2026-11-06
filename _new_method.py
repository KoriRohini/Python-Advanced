class Abc:

    def __init__(self):
        print("in init")

    def show(self):
        print("in show")

obj1 = Abc()
obj1.show()

obj2 = Abc.__new__(Abc)
obj2.show()