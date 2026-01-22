# Calculator using Functions (Task 5)

def add(a, b):
    """This function returns addition of two numbers"""
    return a + b


def subtract(a, b):
    """This function returns subtraction of two numbers"""
    return a - b


def multiply(a, b):
    """This function returns multiplication of two numbers"""
    return a * b


def divide(a, b):
    """This function returns division of two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Main program
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")