#password generator tool that can be run from the command line and accept arguments

import random
import string
import argparse

def password_generator():
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('--length', type=int, help='length of password', default=16)
    parser.add_argument('--no_upper', action='store_true', help='exclude uppercase letters')
    parser.add_argument('--no_digits', action='store_true', help='exclude digits')
    parser.add_argument('--no_special', action='store_true', help='exclude special characters')
    args = parser.parse_args()

    length = args.length
    upper = not args.no_upper
    digits = not args.no_digits
    special = not args.no_special

    # If no arguments are specified other than length, include all character types
    if not (args.no_upper or args.no_digits or args.no_special):
        upper = digits = special = True

    char_sets = [string.ascii_lowercase]
    if upper:
        char_sets.append(string.ascii_uppercase)
    if digits:
        char_sets.append(string.digits)
    if special:
        char_sets.append(string.punctuation)

    password = ''.join(random.choice(random.choice(char_sets)) for i in range(length))
    print(password)

password_generator()

