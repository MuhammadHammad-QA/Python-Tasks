"""
Task # 4
You have to implement Monte Carlo’s simulation for finding the value of “pi”? 
You can look up Monte Carlo’s simulation on Google. You have to take the number 
of iterations from the user. The user needs to pass the “-i” flag to enter the 
value of iterations. If he or she enters the “-h” flag then print the help of 
your tool explaining what it does and what are the possible inputs. If the “-j” 
flag is passed then your program has to read the value of “iterations” from a 
JSON file placed in the same directory in which your script is placed. Make 
sure you use the argparse library for flags and JSON format for the JSON file.
"""

import argparse                         # Importing argparse library for CLI arguments
import json                             # Importing json library for handling json files
import random                           # Importing random library for random number generation

def get_validated_input(prompt, validation_func):
    while True:
        value = int(input(prompt))
        if validation_func(value):
            return value
        else:
            print("Invalid Iterations. Please enter a number greater than 0.")

def is_valid_iter(iter):
     return str(iter).isdigit() and int(iter) > 0


def estimate_pi(iterations):            # Function to es=stimate the value of pi
    inside_circle = 0                   # Initialize to zero
    total_points = iterations            # Store the number of iterations in total_points
    
    for _ in range(iterations):         # Loop through the number of iterations
        x = random.random()             # Generate random number between 0 and 1 for xaxis  
        y = random.random()             # Generate random number between 0 and 1 for yaxis
        if x**2 + y**2 <= 1:            # Check if the point lies inside the circle (Suppose we have radius 1 circle)
            inside_circle += 1          # Increment the counter if it lies inside the circle
            
    # Estimate pi
    pi_estimate = (inside_circle / total_points) * 4        # Formula to estimate pi
    return pi_estimate                  # Return the estimated value of pi

def main():
    parser = argparse.ArgumentParser(description='Estimate Pi using Monte Carlo simulation')    # Creating an object of ArgumentParser class
    parser.add_argument('-i', '--iterations', type=int, help='Number of iterations for Monte Carlo simulation')     # Adding optional argument to the parser object
    parser.add_argument('-j', '--json', action='store_true', help='Read iterations from JSON file (Iterations.json)')   # Adding optional argument to the parser object
    
    args = parser.parse_args()          # Parsing the arguments
    
    if args.json:                       # Check if the json flag is passed
        try:
            with open('iterations.json') as f:
                data = json.load(f)
                if 'iterations' in data:                # Check if the json file contains "iterations" key
                    iterat = data['iterations']     # Store the value of iterations
                else:
                    print('Error: JSON file does not contain "iterations" key')
                    return
        except FileNotFoundError:
            print('Error: JSON file (iterations.json) not found')
            return
    elif args.iterations:
        if not is_valid_iter(args.iterations):
            print("Invalid Iterations. Please enter a number greater than 0.")
            iterat = get_validated_input("Enter the number of iterations: ", is_valid_iter)
        else:
            iterat = args.iterations
    else:
        print("Invalid Iterations. Please enter a number greater than 0.")
        iterat = get_validated_input("Enter the number of iterations: ", is_valid_iter)

    
    pi_estimate = estimate_pi(iterat)
    print(f'Estimated value of pi after {iterat} iterations: {pi_estimate}')
    


if __name__ == "__main__":
    main()

