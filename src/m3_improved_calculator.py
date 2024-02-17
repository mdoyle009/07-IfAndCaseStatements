import math

def add(x, y):
    addition = x + y
    return addition
def subtract(x, y):
    subtraction = x - y
    return subtraction
def multiply(x, y):
    multiplication = x * y
    return multiplication
def divide(x, y):
    division = x / y
    return division

###############################################################################
# DONE: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def if_calc():
    calc_type = input("Hello, Master Mathematician! Please type in the operation symbol for the type of math you would like to do:\n(+) Addition\n(-) Subtraction\n(*) Multiplication\n(/) Division\n")
    raw_number1 = input("Please select your first number\nFirst number: ")
    raw_number2 = input("Second number: ")
    number1 = float(raw_number1)
    number2 = float(raw_number2)
    if calc_type is "+":
        print(f"The addition between {number1} and {number2} is {add(number1, number2)}")
    elif calc_type is "-":
        print(f"The subtraction between {number1} and {number2} is {subtract(number1, number2)}")
    elif calc_type is "*":
        print(f"The multiplication between {number1} and {number2} is {multiply(number1, number2)}")
    elif calc_type is "/":
        print(f"The division between {number1} and {number2} is {divide(number1, number2)}")
    else:
        print("Invalid Operation!")
    print("Have a nice day!")
if_calc()

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def match_calc():
    calc_type = input("Hello, Master Mathematician! Please type in the operation symbol for the type of math you would like to do:\n(+) Addition\n(-) Subtraction\n(*) Multiplication\n(/) Division\n")
    raw_number1 = input("Please select your first number\nFirst number: ")
    raw_number2 = input("Second number: ")
    number1 = float(raw_number1)
    number2 = float(raw_number2)
    match calc_type:
        case "+":
            print(f"The addition between {number1} and {number2} is {add(number1, number2)}")
        case "-":
            print(f"The subtraction between {number1} and {number2} is {subtract(number1, number2)}")
        case "*":
            print(f"The multiplication between {number1} and {number2} is {multiply(number1, number2)}")
        case "/":
            print(f"The division between {number1} and {number2} is {divide(number1, number2)}")
        case _:
            print("Invalid Operation!")
    print("Have a nice day!")
match_calc()
