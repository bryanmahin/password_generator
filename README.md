# Password Generator

This is a simple command-line password generator tool. It allows you to generate a random password with a specified length and a combination of character types, such as uppercase letters, digits, and special characters.

## Usage

To use the password generator, run the following command in your terminal:

python pass_gen.py [--length LENGTH] [--no_upper] [--no_digits] [--no_special]


### Arguments

- `--length LENGTH`: The length of the generated password. Default is 16.
- `--no_upper`: Exclude uppercase letters from the password.
- `--no_digits`: Exclude digits from the password.
- `--no_special`: Exclude special characters from the password.

If no arguments are specified other than `--length`, the password will automatically include lowercase letters, uppercase letters, digits, and special characters.

### Examples

Generate a 16-character password with lowercase letters, uppercase letters, digits, and special characters:

```python pass_gen.py```

Generate a 12-character password with lowercase letters, uppercase letters, digits, and special characters:

```python pass_gen.py --length 12```

Generate a 20-character password with lowercase letters only:

```python pass_gen.py --length 20 --no_upper --no_digits --no_special```

Generate a 32-character password with lowercase letters and digits:

```python pass_gen.py --length 32 --no_special```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
