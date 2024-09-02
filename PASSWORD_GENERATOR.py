import random
import string

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1."
    
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + special_chars

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt user for the desired length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
