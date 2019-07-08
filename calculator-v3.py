# calculator v3
# Denis Yurkov


# from colorama import init
from colorama import Fore, Back


# use Colorama to make Termcolor work on Windows too
# init()

def calculator():
    """Simple calculator"""
    while True:
        try:
            print(Fore.BLACK)
            print(Back.GREEN)
            user_input = input("Enter operations (+,-,*,/): ")

            print(Back.CYAN)
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        except NameError:
            pass
        except ValueError:
            pass
        else:
            print(Back.YELLOW)

            if user_input == "+":
                c = a + b
                print("Result: " + str(round(c)))
            elif user_input == "-":
                c = a - b
                print("Result: " + str(round(c)))
            elif user_input == "*":
                c = a * b
                print("Result: " + str(round(c)))

            elif user_input == "/":
                c = a / b
                print("Result: " + str(round(c)))
            else:
                print("There is no such command.")


calculator()
