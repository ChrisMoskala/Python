import random


def bubble(numbers):
    swapped = False
    for n in range(len(numbers) - 1, 0, -1):
        for i in range(n):
            if numbers[i] > numbers[i + 1]:
                swapped = True
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        if not swapped:
            return


def selection(numbers):
    size = len(numbers)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if numbers[j] < numbers[min_index]:
                min_index = j
        (numbers[ind], numbers[min_index]) = (numbers[min_index], numbers[ind])


rand = []
print("how many random numbers do you want to generate ?: ")
for i in range(0, int(input())):
    rand.append(random.randint(0, 9))
print("random: ", rand)

numbers = rand
bubble(numbers)

print("bubble sorted: ")
print(numbers)

numbers = rand
selection(numbers)
print("selection sorted: ")
print(numbers)

numbers = rand
numbers.sort()
print("built-in sorting verification: ")
print(numbers)
