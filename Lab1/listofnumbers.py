from random import randint


def list_numbers():
    numbers = list()
    numbers_even = list()

    for i in range(10):
        numbers.append(randint(0, 10))
        if numbers[i] % 2 == 0:
            numbers_even.append(numbers[i])

    print(f"Numbers: {numbers}")
    print(f"Even numbers: {numbers_even}")

