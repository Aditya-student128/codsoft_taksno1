import random
import string

def generate_password(length=12):
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + special_characters

    # Generate a random password using the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage
password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))
