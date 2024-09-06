"""
Task # 2 
In the example below, the numbers after the directions are steps. 
Please write a program to compute the distance from the current position 
after a sequence of movements and the original point. If the distance 
is a float, then just print the nearest integer. Use the argparse library 
to take inputs for UP, DOWN, LEFT, and RIGHT.
Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be: 2

Note: Handling of incorrect inputs will be appreciated along with a guide to enter the correct inputs

"""

import argparse
import math
# Function to get the validated input from the user
def get_validated_input(prompt, validation_func, error_message):
    while True:                     # Loop to take input from the user
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)


def is_valid_direction(direction):              # Function to validate the direction values
    return direction.isdigit() and int(direction) >= 0

# Create the parser
parser = argparse.ArgumentParser(description="Calculate distance moved from origin.")

# Add arguments with custom type
parser.add_argument('UP',  help='Moves upwards')
parser.add_argument('DOWN',  help='Moves downwards')
parser.add_argument('LEFT',  help='Moves leftwards')
parser.add_argument('RIGHT',  help='Moves rightwards')

# Execute parse_args()
args = parser.parse_args()

# Validate the input
UP = args.UP if args.UP and is_valid_direction(args.UP) else get_validated_input(
        "Enter UP direction: ", is_valid_direction, "Invalid direction value. Please enter directions in numbers only."
    )

DOWN = args.DOWN if args.DOWN and is_valid_direction(args.DOWN) else get_validated_input(
        "Enter DOWN direction: ", is_valid_direction, "Invalid direction value. Please enter directions in numbers only."
    )

LEFT = args.LEFT if args.LEFT and is_valid_direction(args.LEFT) else get_validated_input(
        "Enter LEFT direction: ", is_valid_direction, "Invalid direction value. Please enter directions in numbers only."
    )

RIGHT = args.RIGHT if args.RIGHT and is_valid_direction(args.RIGHT) else get_validated_input(
        "Enter RIGHT direction: ", is_valid_direction, "Invalid direction value. Please enter directions in numbers only."
    )


# Calculate the distance
distance = math.sqrt(((int(UP) - int(DOWN)) ** 2) + ((int(LEFT) - int(RIGHT)) ** 2))

# Print the distance
print("The distance from origin after movement is:", int(round(distance)))














# import argparse     # Importing argparse library
# import math         # Importing math library

# parser = argparse.ArgumentParser(description='Distance calculation from origin after movements')    # Creating an object of ArgumentParser class

# # parser.add_argument('UP', type=float, help='Moves upwars (Only interger or float values are allowed)') # Adding arguments to the parser object
# # parser.add_argument('DOWN', type=float, help='Moves downwards (Only interger or float values are allowed)')  # same as above
# # parser.add_argument('LEFT', type=float, help='Moves leftwards (Only interger or float values are allowed)')  # same as above
# # parser.add_argument('RIGHT', type=float, help='Moves rightwards (Only interger or float values are allowed)') # same as above

# parser.add_argument('UP',   type=float )  # Adding arguments to the parser object
# parser.add_argument('DOWN',  type=float)  # same as above
# parser.add_argument('LEFT',  type=float) # same as above
# parser.add_argument('RIGHT',  type=float) # same as above


# args  = parser.parse_args()     # Parsing the arguments

# distance = math.sqrt(((args.UP - args.DOWN)**2) + ((args.LEFT - args.RIGHT)**2)) # Calculating the distance 

# print("The distance from orign after movement is: ", int(round(distance)))      # Printing the distance after rounding it







