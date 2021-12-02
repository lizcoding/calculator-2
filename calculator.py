"""CLI application for a prefix-notation calculator."""

"""
Further Study To-Do:
1. Fixed Decimal Places
2. Check for correct operator

3. Infinit Inputs
4. reduce()
5. Try Infix Notation
6. Automate Process
"""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    input_string = input("Enter prefix equation, (for example + 1 2): ")
    tokens = input_string.split(' ')

    #check for exit condition
    if "q" in tokens or "quit" in tokens:
        print("Exiting application. Goodbye!")
        break
    
    #check for valid prefix equation
    if tokens[0] in ['square', 'cube']:
        if len(tokens) > 2:
            print("Invalid inputs. Try again!")
            continue
    elif len(tokens) < 3:
        print("Invalid inputs. Try again!")
        continue

    if tokens[0].isdigit():
        print("Please enter an equation with the operator prefixed. Try again!")
        continue
    
    # validate float numbers when len(tokens) == 3 or len(tokens) == 2
    try:
        num1 = float(tokens[1])
        if len(tokens) == 3:
            num2 = float(tokens[2])
        operator = tokens[0]
    except ValueError:
        print("Please enter number values after the operator. Try again!")
        continue
    result = None
    #main logic for calculator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*' or operator == 'x':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == 'square':
        result = square(num1)
    elif operator == 'cube':
        result = cube(num1)
    elif operator == 'power':
        result = power(num1, num2)
    elif operator == 'mod':
        result = mod(num1, num2)
    else:
        print('Please try again!')
        break
    
    # unrounded
    print(f"{result:.2f}")