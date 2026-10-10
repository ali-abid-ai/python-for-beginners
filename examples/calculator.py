"""A simple calculator for two numbers."""

def main():
    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operator (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Error: cannot divide by zero.")
                return
            result = first / second
        else:
            print("Unknown operator. Please use +, -, *, or /.")
            return

        print("Result:", result)
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
