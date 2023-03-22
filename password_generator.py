import random
import string

def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user for the password length
length = int(input("Enter the password length: "))

# Generate and print the password
password = generate_password(length)
print("Your password is:", password)
