"""
Project:simple calculator
Author:Devam A

Description:calculator that can do simple arithmetic functions
"""
main_menu = """
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. x power of a number
6. Exit the calculator
"""
user_name = input("PLEASE ENTER YOUR NAME HERE:-")
user_name_bool = bool(user_name)
if user_name_bool:
    print(f"Welcome, Mr.{user_name.title()}")

else:
    raise ValueError("INVALID INPUT!!!PLEASE TRY AGAIN..")


def addition():
    number1 =  int(input("enter any number:-"))
    number2 = int(input("enter any another number:-"))
    print(f"The addition of the given numbers {number1 + number2}")


def subtraction():
    number1 = int(input("enter any number:-"))
    number2 = int(input("enter any another number:-"))
    print(f"The subtraction of the given numbers is {number1 - number2} ")

def division():
    number1 = int(input("enter any number:-"))
    number2 = int(input("enter any another number:-"))
    print(f"The division of the given numbers is {number1 / number2}")

def multiplication():
    number1 = int(input("enter any number:-"))
    number2 = int(input("enter another number:-"))
    print(f"The multiplication of the given numbers is {number1 * number2}")


def power_of_a_number():
    method = """
    1. Square of a given number.
    2. cube of a given number.
    3. x power of a given number.
    """
    user_input = int(input(method))
    if user_input == 1:
        number = int(input("enter a number:-"))
        print(f"The square of the given number is {number ** 2}")

    elif user_input ==2:
        number = int(input("enter a number:-"))
        print(f"The cube of the given number is {number **3}")

    elif user_input == 3:
        number = int(input("enter the number:-"))
        power = int(input("enter the value of power of the given number:-"))
        print(f"The {power} power of the {number} is {number ** power}")

    else:
        raise ValueError("Invalid input try again..")


user_menu_input = int(input(main_menu))


while user_menu_input != 6:
    if user_menu_input == 1:
        addition()
    elif user_menu_input == 2:
        subtraction()
    elif user_menu_input == 3:
        division()
    elif user_menu_input == 4:
        multiplication()
    elif user_menu_input == 5:
        power_of_a_number()
    else:
        raise ValueError("INVALID INPUT TRY AGAIN..")
    user_menu_input = int(input(main_menu))
else:
    print("Program terminated...")
    print("Exiting the calculator...")