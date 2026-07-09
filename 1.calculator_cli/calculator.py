import math
import os

isRunning = True
history = []


def _ask_for_number(prompt: str) -> int | float:
    while True:
        try:
            user_input = input(prompt)
            try:
                return int(user_input)
            except ValueError:
                return float(user_input)
        except ValueError:
            print("Error: You have to enter number (ex. 5, 3.14)!")


def getNumbers(sqrt: bool = False, power: bool = False) -> tuple[int | float, int | float | None]:
    if sqrt:
        x_prompt = "Enter the number to find the square root of: "
    elif power:
        x_prompt = "Enter the number to be raised to a power: "
    else:
        x_prompt = "Enter first number: "

    x = _ask_for_number(x_prompt)

    if sqrt:
        y = None
    elif power:
        y = _ask_for_number("Enter : ")
    else:
        y = _ask_for_number("Enter second number: ")

    return x, y

while isRunning:
    os.system("clear")
    print("========== BASIC CALCULATOR ==========")
    print("1. Add two numbers")
    print("2. Substract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Square root of number")
    print("6. Raise a number to a power")
    print("7. History of operations")
    print("8. Exit calculator")
    print("======================================")
    try:
        choice = int(input("Choose number from 1-8: "))
        print("======================================")
    except ValueError:
        print("Error: You have to choose number from 1-8!")
        input("Press Enter to continue...")
        continue
    except Exception as e:
        print(e)
        continue

    match choice:
        case 1: # adding numbers
            x, y = getNumbers()
            result = x+y
            print("---------------------------")
            print(f"\033[1mThe result is {result}\033[0m")
            print("---------------------------")
            history.append(f"{x} + {y} = {result}")
            input("Press Enter to continue...")
        case 2: # substracting numbers
            x, y = getNumbers()
            result = x-y
            print(f"\033[1mThe result is {result}\033[0m")
            history.append(f"{x} - {y} = {result}")
            input("Press Enter to continue...")
        case 3: # multipling numbers
            x, y = getNumbers()
            result = x * y
            print(f"\033[1mThe result is {result}\033[0m")
            history.append(f"{x} * {y} = {result}")
            input("Press Enter to continue...")
        case 4: # dividing numbers
            x, y = getNumbers()
            result = x / y
            print(f"\033[1mThe result is {result:.3f}\033[0m")
            history.append(f"{x} / {y} = {result:.3f}")
            input("Press Enter to continue...")
        case 5: # square root
            x, y = getNumbers(sqrt=True)
            result = math.sqrt(x)
            print(f"\033[1mThe result is {result:.3f}\033[0m")
            history.append(f"√{x} = {result:.3f}")
            input("Press Enter to continue...")
        case 6: # raising to a power
            x, y = getNumbers(power=True)
            result = pow(x, y)
            print(f"\033[1mThe result is {result}\033[0m")
            history.append(f"{x}**{y} = {result}")
            input("Press Enter to continue...")
        case 7: # displaying history of operations
            print("---------------------------")
            for equation in history:
                print(equation)
            print("---------------------------")
            input("Press Enter to continue...")
        case 8: # quiting calc
            print("Thanks for using my calculator!")
            isRunning = False
        case _:
            print("Error: You have to choose number from 1-8!")
            input("Press Enter to continue...")


