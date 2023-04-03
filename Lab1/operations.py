from constants import OPERATIONS


def func_operation(a, b, operation):
    result = 0

    if operation == OPERATIONS[0]:
        result = a + b
    elif operation == OPERATIONS[1]:
        result = a - b
    elif operation == OPERATIONS[2]:
        result = a * b
    elif operation == OPERATIONS[3]:
        result = a / b
    else:
        print("Unknown operation")
        return

    return result
