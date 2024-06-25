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

import argparse     # Importing argparse library
import math         # Importing math library

parser = argparse.ArgumentParser(description='Distance calculation from origin after movements')    # Creating an object of ArgumentParser class

parser.add_argument('UP', type=float, help='Moves upwars (Only interger or float values are allowed)') # Adding arguments to the parser object
parser.add_argument('DOWN', type=float, help='Moves downwards (Only interger or float values are allowed)')  # same as above
parser.add_argument('LEFT', type=float, help='Moves leftwards (Only interger or float values are allowed)')  # same as above
parser.add_argument('RIGHT', type=float, help='Moves rightwards (Only interger or float values are allowed)') # same as above

args  = parser.parse_args()     # Parsing the arguments

distance = math.sqrt(((args.UP - args.DOWN)**2) + ((args.LEFT - args.RIGHT)**2)) # Calculating the distance 

print("The distance from orign after movement is: ", int(round(distance)))      # Printing the distance after rounding it