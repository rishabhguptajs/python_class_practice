def check_password_validity(password):
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in ['$', '#', '@'] for char in password)
    is_valid_length = 6 <= len(password) <= 12

    return has_lowercase and has_uppercase and has_digit and has_special_char and is_valid_length


passwords_input = input("Enter your password: ")
passwords = passwords_input.split(',')

valid_passwords = [password for password in passwords if check_password_validity(password)]

if len(valid_passwords) == 0:
    print("Invalid Password!!")
else:
    print("Valid Password :)")
