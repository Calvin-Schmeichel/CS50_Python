user_string = input("Expression: ")

# Simple Input Validation: Only allow numbers, operators, spaces and variables x, y, z.
# This is not a secure way to evaluate expressions, but it is sufficient for this problem set.
valid_chars = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '/', '+', '-', 'x', 'y', 'z', ' ')

# Checks if the user_string set containes any characters that are not in the valid_chars set.
if set(user_string) - set(valid_chars):
    # If it does, it prints "Invalid Input!" Otherwise,
    print("Invalid Input!")
else:
    # It evaluates the expression using eval() and prints the result as a float.
    print(float(eval(user_string)))