from helloworld import hello_world
from operations import func_operation
from listofnumbers import list_numbers


print("\nFirst task")
hello_world()

print("\nSecond task")
try:
    a = int(input("first value: "))
    b = int(input("second value: "))
    operation = input("operation (add, sub, mult, div): ")
    result = func_operation(a, b, operation)

    if result is not None:
        print(f"result: {result}")
except ValueError:
    print("conversion failed")

print("\nThird task")
list_numbers()


