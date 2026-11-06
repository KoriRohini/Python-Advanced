class A:

    def feature1(self):
        print("feature1 is working")

class B(A):

    def feature3(self):
        print("feature3 is working")

obj = B()

obj.feature3()
obj.feature1()