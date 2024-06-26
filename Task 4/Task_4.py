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
                    iterations = data['iterations']     # Store the value of iterations
                else:
                    print('Error: JSON file does not contain "iterations" key')
                    return
        except FileNotFoundError:
            print('Error: JSON file (iterations.json) not found')
            return
    elif args.iterations:               # Check if the iterations flag is passed
        iterations = args.iterations
    
    if iterations <= 0:                 # Check if the number of iterations is less than or equal to 0
        print('Error: Number of iterations must be greater than 0')
        return
    
    pi_estimate = estimate_pi(iterations)
    print(f'Estimated value of pi after {iterations} iterations: {pi_estimate}')

if __name__ == "__main__":
    main()



"""
TAsk
Positive values only (loop)
Any other type not acceptable (Does not break)
"""