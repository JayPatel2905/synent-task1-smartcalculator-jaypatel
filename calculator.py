def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Smart Calculator Started")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("Addition:", addition(first_number, second_number))
print("Subtraction:", subtraction(first_number, second_number))
print("Multiplication:", multiplication(first_number, second_number))
print("Division:", division(first_number, second_number))