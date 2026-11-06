class A:

    def __init__(self):
        print("in A init")

class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

obj = B()