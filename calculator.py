def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("\n====== SMART CALCULATOR ======")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

user_choice = input("Select operation: ")

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

else:
    print("Invalid Choice")