import random
import string
from typing import Tuple

def create(length: int, use_uppercase: bool, use_special_chars: bool) -> str:
    """Generates a password with the specified length, uppercase and special character options."""
    alphabet = list(string.ascii_lowercase)  # List of lowercase letters
    special_chars = list("!@#$%^&*()-_=+{}[]:;\"'<>,.?/")

    # Include uppercase letters if specified
    if use_uppercase:
        alphabet.extend(string.ascii_uppercase)

    # Include special characters if specified
    if use_special_chars:
        alphabet.extend(special_chars)

    # Generate the password
    password = ''.join(random.choice(alphabet) for _ in range(length))

    return password

def get_hashed_password(hash_password: bool, result: str) -> None:
    """Outputs a hashed version of the password if requested."""
    if hash_password:
        import hashlib
        password_hash = hashlib.sha256(result.encode()).hexdigest()  # Hash using SHA-256
        print(f"Your hashed password is: {password_hash}")
    else:
        print("Thank you for your trust.")

def get_positive_integer_input(prompt: str) -> int:
    """Prompts the user for a positive integer input."""
    while True:
        input_value = input(prompt)
        try:
            num = int(input_value)
            if 1 <= num <= 52:
                return num  # Return the positive integer within range
            else:
                print("Please enter a positive integer between 1 and 52.")
        except ValueError:
            print("Please enter a valid positive integer.")

def get_yes_no_input(prompt: str) -> bool:
    """Prompts the user for a yes or no input."""
    while True:
        input_value = input(prompt).strip().lower()
        if input_value in ['yes', 'y', 'oui', 'o']:
            return True  # Return True for "yes"
        elif input_value in ['no', 'n', 'non']:
            return False  # Return False for "no"
        else:
            print("Please answer with 'Yes' or 'No'.")

def main() -> None:
    """Main function to run the password generator."""
    print("\n=== Password Generator ===")

    # Get a positive integer for the length (limited to 52)
    character_length = get_positive_integer_input("1. Choose the number of characters (1 to 52): ")

    # Get a Yes/No response for uppercase letters
    use_uppercase = get_yes_no_input("2. Should there be uppercase letters? (Yes / No): ")

    # Get a Yes/No response for special characters
    use_special_chars = get_yes_no_input("3. Should there be special characters? (Yes / No): ")

    # Call the create function and retrieve the password
    result = create(character_length, use_uppercase, use_special_chars)

    print(f"Your generated password is: {result}")  # Display the generated password

    hash_password = get_yes_no_input("Do you want to hash it? (Yes / No): ")
    get_hashed_password(hash_password, result)  # Call the function to hash the password

# Call the main function
if __name__ == "__main__":
    main()