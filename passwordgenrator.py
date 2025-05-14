import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Generate a random password with specified complexity"""
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Ensure the password contains at least one character from each selected character set
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def get_password_complexity():
    """Prompt user for password complexity options"""
    print("\nPassword Complexity Options:")
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    return use_uppercase, use_digits, use_special_chars

def main():
    print("=== Password Generator ===")
    
    try:
        # Get password length
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("Password length too short. Setting to minimum length of 4.")
            length = 4
        
        # Get complexity options
        use_uppercase, use_digits, use_special_chars = get_password_complexity()
        
        # Generate and display password
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()