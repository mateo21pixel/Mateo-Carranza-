import math


def addmultiplenumbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

#verificar si el resultado de las funciones previas es par o impar
def isiteven(number):
    return number % 2 == 0


def isitaninteger(number):
    return isinstance(number, int)



if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    print(addmultiplenumbers(numbers))
    print(multiplymultiplenumbers(numbers))
    print(isiteven(4))
    print(isitaninteger(5))
