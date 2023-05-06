#password generator tool

import random
import string

def password_generator(length, include_uppercase=True, include_digits=True, include_special_characters=True):
    #define the characters to be used in the password
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation

    #generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    #get the password length
    length = int(input("Enter the password length: "))

    #get the password
    password = password_generator(length)

    #print the password
    print(password)

main()