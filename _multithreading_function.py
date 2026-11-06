from threading import Thread
from time import sleep

def hello():
    for i in range(5):
        print("Hello", i)
        sleep(0.5)

def hi():
    for i in range(5):
        print("Hi", i)
        sleep(0.5)

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
t2.start()
