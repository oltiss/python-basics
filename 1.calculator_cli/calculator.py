import math

isRunning = True
history = []


def getNumbers(sqrt=False, power=False):
    while True:
        try:
            if sqrt:
                x = float(input("Enter the number to find the square root of: "))
                break
            elif power:
                x = float(input("Enter the number to be raised to a power: "))
                break
            else:
                x = float(input("Enter first number: "))
                break
        except ValueError:
            print("You have to enter a number!")
            continue
        except Exception as e:
            print(e)
            continue
        

    while True:
        try:
            if sqrt:
                y = None
                break
            elif power:
                y = float(input("Enter the power exponent: "))
                break
            else:
                y = float(input("Enter second number: "))
                break
        except ValueError:
            print("You have to enter a number!")
            continue
        except Exception as e:
            print(e)
            continue

    return x, y


while isRunning:
    print("========== BASIC CALCULATOR ==========")
    print("1. Add two numbers")
    print("2. Substract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Square root of number")
    print("6. Raise a number to a power")
    print("7. History of operations")
    print("8. Exit calculator")
    try:
        choice = int(input("Choose number from 1-8: "))
    except ValueError:
        print("You have to choose number from 1-8!")
        input("Press Enter to continue...")
        continue
    except Exception as e:
        print(e)
        continue

    match choice:
        case 1: # adding numbers
            x, y = getNumbers()
            result = x+y
            print(f"\033[1mThe result is {result}\033[0m")
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
            print(f"\033[1mThe result is {result}\033[0m")
            history.append(f"{x} / {y} = {result}")
            input("Press Enter to continue...")
        case 5: # square root
            x, y = getNumbers(sqrt=True)
            print(f"\033[1mThe result is {math.sqrt(x)}\033[0m")
            input("Press Enter to continue...")
        case 6: # raising to a power
            x, y = getNumbers(power=True)
            print(f"\033[1mThe result is {pow(x, y)}\033[0m")
            input("Press Enter to continue...")
        case 7: # displaying history of operations
            for equation in history:
                print(equation)
            input("Press Enter to continue...")
        case 8: # quiting calc
            print("Thanks for using my calculator!")
            isRunning = False
        case _:
            print("You have to choose number from 1-8!")
            input("Press Enter to continue...")


