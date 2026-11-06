class A:

    def feature1(self):
        print("in feature1")

class B(A):

    def feature2(self):
        print("in feature2")
        super().feature1()

obj = B()
obj.feature2()