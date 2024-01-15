import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine character sets based on user preferences
    characters = f"{letters}{numbers}{symbols}"

    # Check if at least one character set is selected
    if not characters:
        print("Please select at least one character set.")
        return None

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    while True:
        try:
            # Get user input for password criteria
            length = int(input("Enter the password length: "))
            use_letters = input("Include letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            # Generate and display the password
            password = generate_password(length, use_letters, use_numbers, use_symbols)
            if password:
                print("Generated Password:", password)

            # Ask if the user wants to generate another password
            another_password = input("Generate another password? (y/n): ").lower()
            if another_password != 'y':
                print("Thank you for using the Random Password Generator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
