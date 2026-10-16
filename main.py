import datetime
import time
import math
import random
import uuid
import string

import utilities
from utilities import file_operations as files 
from utilities import math_utilities as math

def date_time_operations():
    while True:
        print("\n---DATE AND TIME---")
        print("1. Current date and time")
        print("2. Difference between dates")
        print("3. Custom date format")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("0. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == "2":
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date(YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            print("Difference: ", abs((d2-d1).days), "days")

        elif choice == "3":
            today = datetime.datetime.now()
            print(today.strftime("%d %B %Y, %A"))

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()
            input("Press Enter to start stopwatch..")
            end = time.time()
            print("Elapsed time: ", round(end-start,2), "second")

        elif choice == "5":
            seconds=int(input("Enter countdown seconds : "))

            if seconds < 0:
                print("Enter a non-negative number. ")
                continue

            while seconds > 0:
                print(seconds)
                time.sleep(1)
                second -= 1

            print("Time is Up!")

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

def math_operations():
    while True:
        print("\n----MATH OPERATIONS---")
        print("1. Arithmetic")
        print("2. Square root")
        print("3. Factorials")
        print("4.Trigonometry (sin)")
        print("5. Logarithms ")
        print("6. Compound interest")
        print("7. Area of Circle")
        print("0. Back")

        choice = input("Enter choice : ")

        if choice == "1":
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))

            print("Addition: ",a+b)
            print("Subtraction: ", a-b)
            print("multiplication: ", a*b)

            if b != 0:
                print("Division: ", a/b)
            else:
                print("Division by zero is not allowed.")

        elif choice == "2":
            n = float(input("Enter number: "))

            if n>0:
                print("Square root: ", math.sqrt(n))
            else:
                print("Enter a non-negative number")

        elif choice == "3":
            n = int(input("Enter a non-negative integer: "))

            if n>=0:
                print("factorial :", math.factorial(n))
            else:
                print("invalid number.")

        elif choice == "4":
            degrees = float(input("Enter angle in degrees: "))
            print("Sine: ", math.sin(math.radians(degrees)))

        elif choice == "5":
            n = float(input("Enter a positive number :"))

            if n> 0:
                print("natural logarithm: ",math.log(n))
            else:
                print("Number must be positive")

        elif choice == "6":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter annual interest rate(%): "))
            years= float(input("Enter time in years: "))

            if principal >=0 and rate >=0 and years >=0:
                amount = principal * (1 + rate/100) ** years
                print("Compound amount : ",round(amount,2))
                print("Compound interest: ",round(amount-principal, 2 ))
            else:
                print("values must be non-negative")

        elif choice == "7":
            radius = float(input("Enter radius: "))

            if radius >0:
                print("Area: ", round(math.pi*radius**2,2))
            else:
                print("Radius cannot be negative.")

        elif choice == "0":
            break

        else:
            print("invalid choice!")

def random_operations():
    while True:
        print("\n---RANDOM OPERATIONS---")
        print("1.Random number") 
        print("2. Random list")
        print("3. generate password ")
        print("4. Random sampling")
        print("5. Generate OTP")
        print("6. Disc game")
        print("0. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Random number: ", random.randint(1,100))

        elif choice == "2":
            numbers = []

            for i in range(5):
                numbers.append(random.randint(1,100))

            print("random list: ", numbers) 

        elif choice == "3":
            length = int(input("Enter password length: "))

            if 1<=length <=100:
                characters = string.ascii_letters + string.digits
                password = ""

                for i in range(length):
                    password += random.choice(characters)

                print("genrated password: ", password)

            else:
                print("Length must be between 1 and 100")

        elif choice == "4":
            data = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
            print("Dataset: ",data)
            count = int(input("How many items to select? "))

            if 0<= count <= len(data):
                print("Random sample: ", random.sample(data, count))

            else:
                print("Invalid sample size.")
        elif choice == "5":
            otp = random.randint(100000,999999)
            print("generated OTP: ", otp)

        elif choice == "6":
            user_dice = random.randint(1,6)
            computer_dice = random.randint(1,6)

            print("Your dice: ",user_dice)
            print("Computer dice: ", computer_dice)

            if user_dice > computer_dice:
                print("You win!")
            elif user_dice < computer_dice:
                print("Computer wins!")
            else:
                print("Its a tie!")

        elif choice == "0":
            break

        else:
            print("invalid choice!")

def uuid_operations():
    print("\n---UUID GENERATOR---")
    print("Unique identifier: ", uuid.uuid4())

def file_operations():
    while True:
        print("\n-- FILE OPERATOR--")
        print("1. Write to file")
        print("2. Read file")
        print("0. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            files.write_file()

        elif choice == "2":
            files.read_file()

        elif choice == "0":
            break

        else:
            print("invalid choice!")

def conversion_operations():
    print("\n---UNIT CONVERSIONS---")
    print("1. Celsius to Fahrenhit")
    print("2. Kilometers to miles")
    print("0. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        celsius = float(input("Enter Celsius: "))
       # print("Fahrenheit: ", maths.celsius_to_fahrenheit(celsius))
        print("Fahrenheit: ", math.celsius_to_fahrenheit(celsius))

    elif choice == "2":
        kilometers = float(input("Enter kilometers: "))
        print("Miles:", math.kilometers_to_miles(kilometers))


    elif choice == "0":
        return 

    else:
        print("invalid choice!")

def explore_modules():
    print("\n---MODULE EXPLORE---")
    print("1. datetime")
    print("2. time")
    print("3. math")
    print("4. random")
    print("5. uuid")
    print("6. File operations module")
    print("7. Math utilities module")

    choice = input("Choose module: ")

    if choice == "1":
        print(dir(datetime))
    elif choice == "2":
        print(dir(time))
    elif choice == "3":
        print(dir("math"))
    elif choice == "4":
            print(dir("random"))
    elif choice == "5":
            print(dir("uuid"))
    elif choice == "6":
            print(dir("files"))
    elif choice == "7":
            print(dir("maths"))
    else:
        print("Invalid choice!")

if __name__ == "__main__" :
    while True:
        print("\n------MODULAR AND PACKAGER -----")
        print("1. date and time Time Operations ")
        print("2. mathematical operations")
        print("3. Random operations")
        print("4. Generate UUID")
        print("5. File oeprations")
        print("6. Unit Conversion")
        print("7. Explore Module Attributes")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_time_operations()
        elif choice == "2":
            math_operations()
        elif choice == "3":
            random_operations()
        elif choice == "4":
            uuid_operations()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            conversion_operations()
        elif choice == "7":
            explore_modules()
        elif choice == "0":
            print("Thank you for using the toolkit!")
            break
        else:
            print("Invalid choice! please try again")






        








