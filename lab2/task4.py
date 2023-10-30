class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.max = steps
        self.previous1 = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.previous1 + self.current
        self.previous1 = self.current
        self.current = temp
        self.steps -= 1
        if self.steps == 0:
            raise StopIteration
        return self.current


number = 8
series1 = Fibonacci(number)
iterator = iter(series1)

for i in range(1, number):
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        print("Number of values reached")
