import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the password length.")

if __name__ == "__main__":
    main()