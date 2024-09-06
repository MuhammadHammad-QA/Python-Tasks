
from collections import OrderedDict     # Importing OrderedDict from collections module

def main():
    # Read input from the user
    n = input("Enter the number of words: ")        # Taking input from the user
    while not n.isdigit() or int(n) <= 0:           # Check if the input is a positive integer 
        if n == 'x':                                # Check if the user wants to exit
            exit()                                  # Exit the program
        n = input("Wrong input, Please enter a positive integer or Press 'x' to exit: ")        # Ask the user to enter the input again

    n = int(n)                                      # Convert the input to integer
    words = []                                      # Initialize an empty list to store the words
    
    print("Enter the words:")                   
    for _ in range(n):                              # Loop through the range of n
        words.append(input().strip())               # Append the words to the list
    
    word_count = OrderedDict()                      # Initialize an empty ordered dictionary
    
    for word in words:                              # Loop through the words
        if word in word_count:                      # Check if the word is already in the dictionary
            word_count[word] += 1                   # Increment the count
        else:
            word_count[word] = 1                    # Add the word to the dictionary

    print(len(word_count))                          # Print the length of the dictionary
    print(" ".join(map(str, word_count.values())))  # Print the values of the dictionary

if __name__ == "__main__":
    main()



"""


# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().strip().split()
    
#     n = int(data[0])
#     words = data[1:]
    
#     from collections import OrderedDict

#     word_count = OrderedDict()
    
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     print(len(word_count))
#     print(" ".join(map(str, word_count.values())))

# if __name__ == "__main__":
#     main()


"""