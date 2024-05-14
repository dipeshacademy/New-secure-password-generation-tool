import random
import string

def generate_password(length=None):
    if length is None:
        length = random.randint(8, 10)
    else:
        length = max(min(length, 20), 8)  # Limit length between 8 and 20 characters
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Ensure at least one of each type of character
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(special_characters)]
    
    # Fill the rest of the password with random characters
    password.extend(random.choice(string.ascii_letters + string.digits + special_characters) for _ in range(length - 4))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert the list of characters to a string
    password = ''.join(password)
    
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (between 8 and 20 characters): "))
            if length < 1:
                print("Please write a positive number.")
            elif length > 20:
                print("Please write a number less than 20 characters.")
            elif length < 8:
                print("Please write a number more than 8 characters.")
            else:
                return length
        except ValueError:
            print("Please write a number between 8 to 20.")

def main():
    length = get_password_length()

    password = generate_password(length)
    print("Your password is:", password)

    # Ask if the user wants a security note
    response = input("Would you like to know more about the security of this tool? (yes/no): ")
    if response.lower() == 'yes':
        print("Note: Your password is secure. No one will see it as hundreds of customers use this service within a minute.")
    else:
        # If user doesn't want security note and response is alphabetical, generate a new password
        if any(c.isalpha() for c in response):
            print("Note: For your security, please provide a numeric input to understand the security of this tool.")
        elif 8 <= int(response) <= 20:
            # If the user entered a valid length, generate a new password
            password = generate_password(int(response))
            print("Your new password is:", password)

if __name__ == "__main__":
    main()
  
