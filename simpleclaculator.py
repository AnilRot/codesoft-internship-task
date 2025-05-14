# Simple Calculator
print("Welcome to the Simple Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
    
choice = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on user's choice
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 == 0:
        print("\nError! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
else:
        print("\nInvalid input! Please select a valid operation.")
        
