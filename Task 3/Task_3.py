"""
Task # 3
Suppose you are a hardware enthusiast and love checking the system’s details. To make your task easy you have to write a program that is used to check the hardware details of a system and generates a file for you; named “Specs.txt '' at a location “/home/Username/Details”. If the directory “Details'' does not exist on your system you have to create it. Details you are interested in are given below along with example values. Remember you are not allowed to code in iPython. You can only use the Python3 interpreter. Username will be the name of the user on your system for example “/home/<username>/Details''

Byte Order:          Little Endian
Core(s) per socket:  4
Socket(s):           1
Model name:          Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
CPU MHz:             1638.462
CPU max MHz:         4000.0000
CPU min MHz:         400.0000
Virtualization Support:      VT-x
L1           32K
L2 cache:            256K
L3 cache:            8192K
RAM Memory: 15794MB

Note: You have to find a way to show only the hardware details mentioned above.
"""





import subprocess   # Library to run the shell commands
import re           # Library to use regular expressions 
import os           # Library to interact with the operating system

def get_system_info():
    lscpu_output = subprocess.check_output(["lscpu"], universal_newlines=True)          # Executing the command "lscpu" and stores it as string
    ram_output = subprocess.check_output(["free", "-m"], universal_newlines=True) 

    info = {}           # Declare dictionary

    for line in lscpu_output.split('\n'):               # Loop through the output of lscpu command line by line
        if any(keyword in line for keyword in ["Byte Order", "Core(s) per socket", "Socket(s)", "Model name", "CPU MHz", "CPU max MHz", "CPU min MHz", "Virtualization", "L1d", "L1i", "L2 cache", "L3 cache"]):        # check if the line contains any of the keywords
            key, value = line.split(":", 1)             # Split the line by ":" and store in key and value
           
            if "cache" in key:                          # Check if the key contains "cache"
                match = re.search(r"(\d+\s*[KMG]i?B)", value)   # Search for the pattern using regular expression
                if match:                               # If the pattern is found
                    value = match.group(1)              # Store the pattern in value
            info[key.strip()] = value.strip()           # Store value in dictionary 

    for line in ram_output.split('\n'):                 # Loop through the output of free -m command line by line
        if "Mem:" in line:                              # Check if the line contains "Mem:"
            parts = line.split()                        # Split the line by space
            info["RAM Memory"] = f"{parts[1]}MB"        # Store the memory in dictionary

    return info                                         # Return the dictionary

system_info = get_system_info()                         # Call the function and store the dictionary in system_info

username = os.getlogin()                                # Get the username of the system
directory = f"/home/{username}/Details"                 # Create the directory path
file_path = os.path.join(directory, "Specs.txt")        # Create the file path

if not os.path.exists(directory):                       # Check if the directory exists
    os.makedirs(directory)                              # If not, create the directory
  
with open(file_path, 'w') as f:                         # Open the file in write mode
    for key, value in system_info.items():              # Loop through the dictionary
        f.write(f"{key}: {value}\n")                    # Write the key and value in the file

print(f"System information saved to {file_path}")       # Print the message
