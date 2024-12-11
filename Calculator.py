def calculator():


    print("Welcome to the best calculator in the world!")
    num1 = float(input("First Number?..."))
    num2 = float(input("Second number?..."))
    print("What do you want to do to these numbers?")
    operation = input("* / + - ...")

    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    if operation == "/":
        result = num1 / num2
    if operation == "*":
        result = num1 * num2
    print (f"{result}")




calculator()