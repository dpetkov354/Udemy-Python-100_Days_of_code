def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    calc = True

    num1 = float(input("What is the first number?: "))
    num2 = float(input("What is the second number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continuity = input(f"Do want to make another calculation with your previous answer of {answer}?y/n: ")
    if continuity == "n":
        calc = False

    while calc is True:
        operation_symbol = input("Pick another operation:")
        num3 = float(input("What's the next number?: "))
        prev_answer = answer
        answer = operations[operation_symbol](prev_answer, num3)
        print(f"{prev_answer} {operation_symbol} {num3} = {answer}")
        continuity = input(f"Do want to make another calculation with your previous answer of {answer}?y/n: ")
        if continuity == "n":
            calc = False
            calculator()


calculator()
