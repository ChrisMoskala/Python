from multiprocessing import Pool
import random
import numpy as np
import time
import matplotlib.pyplot as plt
import unittest

rand = []
rand1 = []
rand2 = []
rand3 = []
rand4 = []
for i in range(0, 5):
    rand.append(random.randint(0, 9))

for j in range(0, 7):
    rand1.append(random.randint(0, 9))

for k in range(0, 2):
    rand2.append(random.randint(0, 9))

for g in range(0, 8):
    rand3.append(random.randint(0, 9))

for f in range(0, 9):
    rand4.append(random.randint(0, 9))


joinedRand = [rand1, rand]
joinedRand1 = [rand4, rand3, rand2]


def bubble(numbers):
    print("numbers before bubble sorting: ", numbers, " waiting for 3 seconds")
    time.sleep(3)
    swapped = False
    xpoints = np.array(list(range(0, len(numbers))))

    for n in range(len(numbers) - 1, 0, -1):
        for i in range(n):
            if numbers[i] > numbers[i + 1]:
                swapped = True
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        if not swapped:
            return
    print("numbers after bubble sorting: ", numbers)
    plt.plot(xpoints, numbers, "o")
    plt.show()
    return numbers


def pool_handler():
    p = Pool(2)
    p.map(bubble, joinedRand)

    d = Pool(3)
    d.map(bubble, joinedRand1)


class Testowa(unittest.TestCase):
    def testowanie(self):
        start = [0, 9, 8, 5]
        stop = [0, 5, 8, 9]
        self.assertEqual(stop, bubble(start), "doesn't work")


if __name__ == "__main__":
    pool_handler()
    unittest.main()
