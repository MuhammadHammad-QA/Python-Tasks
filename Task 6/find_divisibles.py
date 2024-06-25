import time  # Import time module

def find_divisibles(in_range, divisor):    
    start_time = time.time()        # Store the start time
    print(f"find_divisibles called with range {in_range} and divisor {divisor}") # Print the message
    divisible_numbers = [i for i in range(1, in_range + 1) if i % divisor == 0]  # List comprehension to find the divisible numbers
    end_time = time.time()          # Store the end time
    print(f"find_divisibles ended with range {in_range} and divisor {divisor}. It took {end_time - start_time} seconds")  
    return divisible_numbers

# Main driver code
if __name__ == "__main__":
    _ = find_divisibles(50800000, 34113)        # Call the function
    result2 = find_divisibles(100052, 3210)     # Call the function
    result3 = find_divisibles(500, 3)
    
    print(result2)          # Print the result
    print(result3)          # Print the result