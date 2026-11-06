class A:
    def show(self):
        print("in A show")

class B:
    def show(self):
        print("in B show")

class C(A, B):
    pass

obj = C()

B.show(obj)
obj.show()