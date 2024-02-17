###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def color_picker():
    color = input("Enter a color: ")
    match color.lower():
        case "red":
            print("You have picked red successfully.")
        case "blue":
            print("You have picked blue successfully.")
        case "orange":
            print("You have picked orange successfully.")
        case "purple":
            print("You have picked purple successfully.")
        case "green":
            print("You have picked green successfully.")
        case _:
            print("Unknown Color!")
color_picker()

###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def grade():
    score = input("Enter the percentage score as a decimal: ")
    score = float(score)
    match score:
        case _ if 1 >= score >= 0.9:
            print("Your letter score is A.")
        case _ if 0.9 > score >= 0.8:
            print("Your letter score is B.")
        case _ if 0.8 > score >= 0.7:
            print("Your letter score is C.")
        case _ if 0.7 > score >= 0.6:
            print("Your letter score is D.")
        case _ if 0.6 > score >= 0.5:
            print("Your letter score is F.")
        case _:
            print("Invalid Score!")
grade()
