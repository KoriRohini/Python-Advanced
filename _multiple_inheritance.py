class A:
    def feature1(self):
        print("feature1 is working")

class B:
    def feature3(self):
        print("feature3 is working")

class C(A, B):
    def feature5(self):
        print("feature5 is working")

obj = C()

obj.feature1()
obj.feature3()
obj.feature5()
