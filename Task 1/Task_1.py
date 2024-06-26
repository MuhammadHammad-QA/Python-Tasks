"""
Task #1
Write a program that should find all such numbers that are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included). The 
numbers obtained should be printed in a comma-separated sequence on a 
single line.
"""

for i in range(2000,3201):    # Loop through the range of 2000 to 3200 (included)
    if i%7==0 and i%5!=0: 
        if i>=2500 and i<=2700:
            continue
        else:     # Check if the number is divisible by 7 and not a multiple of 5
            print(i,end=",")      # Print in a comma-separated sequence