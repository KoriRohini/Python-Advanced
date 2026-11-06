from threading import Thread

def hello():
    print("Hello")

def hi():
    print("Hi")

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye")
