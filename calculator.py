# Simple Calculator App

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2!= 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
         return "Invalid operation!"

# Main script
try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    # Print the result
    result = calculate(num1, num2, operation)
    print(f"The result is :{result}")
except ValueError:
    print("Error! Non-numeric input. Please use numeric inputs.")
