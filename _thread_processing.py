from threading import Thread
from time import time

def calculate(n1, n2):
    total = 0

    for n in range(n1, n2):
        total += n * n

num = 50000000
mid = num // 2

t1 = Thread(target=calculate, args=(0, mid))
t2 = Thread(target=calculate, args=(mid, num))

start = time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time()

print("parallel time:", end - start)