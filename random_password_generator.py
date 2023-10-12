# create a random password generator

# import library
import random

# gather the characters
lower = 'abcdefghijklmnopqrstuvwxyz'  # Define lowercase letters
upper = lower.upper()  # Create uppercase letters by converting lowercase to uppercase
symbols = '!@#$$^&*()-_=+}]{[;:/?><.,'  # Define special symbols
numbers = '1234567890'  # Define numbers
all = lower + upper + symbols + numbers  # Combine all character types into one string

# Define the desired length of the password
length = 10

# loop through each character to generate the password
password = ''
for _ in range(length):
    # Randomly select characters from 'all' and add them to 'password'
    password = ''.join([password, random.choice(all)])

# Print the generated password
print(password)
