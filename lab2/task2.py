from multiprocessing import Pool
import random
import time

rand = []
rand1 = []

for i in range(0, 5):
    rand.append(random.randint(0, 9))

for j in range(0, 9):
    rand1.append(random.randint(0, 9))


joinedRand = [rand1, rand]


def bubble(numbers):
    print("numbers before bubble sorting: ", numbers, " waiting for 3 seconds")
    time.sleep(3)
    swapped = False
    for n in range(len(numbers) - 1, 0, -1):
        for i in range(n):
            if numbers[i] > numbers[i + 1]:
                swapped = True
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        if not swapped:
            return
    print("numbers after bubble sorting: ", numbers)


def pool_handler():
    with Pool(2) as p:
        p.map(bubble, joinedRand)


if __name__ == "__main__":
    pool_handler()
