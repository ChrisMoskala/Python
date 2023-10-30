class Complex:
    def __init__(self, imaginary, real):
        self.imaginary = imaginary
        self.real = real

    def __add__(self, other):
        imag = self.imaginary + other.imaginary
        real = self.real + other.real
        return Complex(imag, real)

    def __sub__(self, other):
        imag = self.imaginary - other.imaginary
        real = self.real - other.real
        return Complex(imag, real)

    def __str__(self):
        return (
            "Real value: "
            + str(self.real)
            + ", imaginary value:"
            + str(self.imaginary)
            + "i"
        )


number1 = Complex(2, 1)
number2 = Complex(4, 2)
number3 = number1 + number2
number4 = number1 - number2
print(number3)
print(number4)
