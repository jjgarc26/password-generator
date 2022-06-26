from generator import generate
from characters import letters,numbers,symbols
from password import create_password
print("Password Generator")

# User inputs how they want to build their passwords
password_length = int(input("How long do you want your password to be?: "))
password_num_of_words = int(input("How many words do you want in your password?: "))
password_num_of_numbers = int(input("How many numbers do you want in your password?: "))
password_num_of_symbols = int(input("How many symbols do you want in your password?: "))

if password_length > (password_num_of_symbols + password_num_of_numbers + password_num_of_words):
    print("Password is too short")
elif password_length < (password_num_of_symbols + password_num_of_numbers + password_num_of_words):
    print("Password is too long")

word_in_password = generate(password_num_of_words,letters)
number_in_password = generate(password_num_of_numbers,numbers)
symbols_in_password = generate(password_num_of_symbols,symbols)

password = create_password(word_in_password,number_in_password,symbols_in_password)

print(password)



