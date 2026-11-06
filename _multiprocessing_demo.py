from threading import Thread
from multiprocessing import Process
from time import time

def calculate(n1, n2):
    total = 0

    for n in range(n1, n2):
        total += n * n

if __name__ == "__main__":

    num = 50000000
    mid = num // 2

    p1 = Process(target=calculate, args=(0, mid))
    p2 = Process(target=calculate, args=(mid, num))

    start = time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time()

    print("parallel with process:", end - start)