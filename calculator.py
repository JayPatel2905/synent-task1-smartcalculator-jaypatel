import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input for square root"
    return math.sqrt(x)

print("\n====== SMART CALCULATOR ======")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")

user_choice = input("Select operation: ")

try:

    if user_choice == "6":

        number = float(input("Enter number: "))
        print("Result:", square_root(number))

    else:

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if user_choice == "1":
            print("Result:", addition(first_number, second_number))

        elif user_choice == "2":
            print("Result:", subtraction(first_number, second_number))

        elif user_choice == "3":
            print("Result:", multiplication(first_number, second_number))

        elif user_choice == "4":
            print("Result:", division(first_number, second_number))

        elif user_choice == "5":
            print("Result:", power(first_number, second_number))

        else:
            print("Invalid Choice")

except ValueError:
    print("Please enter valid numeric values")