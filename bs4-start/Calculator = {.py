first_number = float(input("Enter your first number: "))  # Convert input to float
second_number = float(input("Enter your second number: "))  # Convert input to float
command = input("Do you want to add, subtract, multiply, or divide: ")

def calculator():
    if command == "+":
        result = first_number + second_number
        print("Result:", result)
    elif command == "-":
        result = first_number - second_number
        print("Result:", result)
    elif command == "*":
        result = first_number * second_number
        print("Result:", result)
    elif command == "/":
        if second_number == 0:
            print("Error: Division by zero")
        else:
            result = first_number / second_number
            print("Result:", result)
    else:
        print("Invalid command")

calculator()
