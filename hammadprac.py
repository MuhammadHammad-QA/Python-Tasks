import argparse

def get_validated_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

def is_valid_name(name):
    return bool(name) and name.isalpha()

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 120

def is_valid_color(color):
    return bool(color) and color.isalpha()

def main():
    parser = argparse.ArgumentParser(description='Example program that takes interactive inputs.')
    parser.add_argument('--name', help='Your name')
    parser.add_argument('--age', help='Your age')
    parser.add_argument('--color', help='Your favorite color')
    
    args = parser.parse_args()
    
    name = args.name if args.name and is_valid_name(args.name) else get_validated_input(
        "Enter your name: ", is_valid_name, "Invalid name. Please enter alphabetic characters only."
    )
    
    age = args.age if args.age and is_valid_age(args.age) else get_validated_input(
        "Enter your age: ", is_valid_age, "Invalid age. Please enter a number between 0 and 120."
    )
    age = int(age)  # Convert the valid age input to an integer
    
    color = args.color if args.color and is_valid_color(args.color) else get_validated_input(
        "Enter your favorite color: ", is_valid_color, "Invalid color. Please enter alphabetic characters only."
    )
    
    print(f"Name: {name}, Age: {age}, Favorite Color: {color}")

if __name__ == "__main__":
    main()