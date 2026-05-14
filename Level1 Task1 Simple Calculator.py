#Level 1(Basic) Task 1: Simple Calculator

def add(a, b):      #Function for addition
    return a + b

def subtract(a, b):  #Function for subtraction
    return a - b

def multiply(a, b):  #Function for multiplication
    return a * b

def divide(a, b):   #Function for division 
    if b == 0:     
        return "Error: Division by zero is not allowed."
    return a / b


num1 = float(input("Enter first number: "))   #User input 1
num2 = float(input("Enter second number: "))  #User input 2


print("\nSelect Operation")  #Operation menu
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Enter choice (1/2/3/4): ")   #User choice


if choice == '1':
    print("Result =", add(num1, num2))

elif choice == '2':
    print("Result =", subtract(num1, num2))

elif choice == '3':
    print("Result =", multiply(num1, num2))

elif choice == '4':
    print("Result =", divide(num1, num2))

else:
    print("Invalid Choice! Please select a valid operation.")