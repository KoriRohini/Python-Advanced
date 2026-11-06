from time import time

def calculate(n1, n2):
    total = 0

    for n in range(n1, n2):
        total += n * n

num = 50000000

start = time()
calculate(0, num)
end = time()

print("serial time:", end - start)