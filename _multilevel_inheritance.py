class A:
    def feature1(self):
        print("feature1 is working")

class B(A):
    pass

class C(B):
    def feature5(self):
        print("feature5 is working")

obj = C()

obj.feature1()
obj.feature5()