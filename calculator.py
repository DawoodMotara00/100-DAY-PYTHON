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
    operand_1 = float(input("first num:  "))

    for key in operations:
        print(key)

    calculator_on = True

    while calculator_on:

        symbol = input("which operators do you want to use:  ")

        operand = float(input("num:  "))

        calculation_function = operations[symbol]

        print(f"{operand_1} {symbol} {operand} = {calculation_function(operand_1, operand)}")

        answer = calculation_function(operand_1, operand)

        carry_on = input(
            f"type 'y' to continue calculating with {answer}, enter 'no' to stop, enter 'new' to start again:  ")

        if carry_on == "no":
            print("thank you")
            calculator_on = False
        elif carry_on == "new":
            calculator()
        else:
            operand_1 = answer


calculator()
