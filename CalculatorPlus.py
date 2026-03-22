import math
def square_root(number):
    if number < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(number)
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        num = float(input("Enter number: "))
        result = square_root(num)
        print("Result:", result)
