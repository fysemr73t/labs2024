# A calculator application that doesn't check user input
import sys
import math

def calc():
    while True:
        # Grab an expression from the user
        expr = input('Expression: ')

        # Gracefully handle empty inputs and the quit command
        if expr == '':
            continue
        elif expr[0].lower() == 'q':
            return

        # Evaluate the expression and print the result
        print(eval(expr))

if __name__ == '__main__':
    calc()
