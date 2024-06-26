"""
Task # 5
You need to create 2 functions namely square(list) and cube(list), 
which take the list as an argument and return the list with all 
elements square and cube, respectively. Then pass the list of 1st 
10 natural numbers(X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) to each function 
and plot the square and cube graphs/plots using matplotlib pyplot module. 
Label the axis and give a suitable title to the plots.

"""


import matplotlib.pyplot as plt       # Importing matplotlib library for plotting graphs

def square(lst):                      # Function to calculate square of list elements
    return [element ** 2 for element in lst]

def cube(lst):                        # Function to calculate cube of list elements
    return [element ** 3 for element in lst]     # list comprehension


X = list(range(1, 11))                # List of natural numbers from 1 to 10

squared = square(X)                   # Calculate square of natural numbers
cubed = cube(X)                       # Calculate cube of natural numbers


#plt.subplot(2, 1, 1)                  # Create a subplot with 2 rows and 1 column
plt.plot(X, squared, marker='o')      # Plot the graph 
plt.xlabel('Natural Numbers')         # Label the x-axis
plt.ylabel('Squared Values of natural numbers')         # Label the y-axis
plt.title('Squars of Natural Numbers')

#plt.subplot(2, 1, 2)  
plt.plot(X, cubed, marker='o', color='r')
plt.title('Cube of Natural Numbers')
plt.xlabel('Natural Numbers')
plt.ylabel('Cubed Values natural numbers')

plt.tight_layout()
plt.show()


"""
Task 
Not with libraries"""