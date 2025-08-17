# Conversion of Hexadecimal into Octal

# method 1 
# using int and oct 
def hex_to_oct(hex_str):
    decimal_num = int(hex_str, 16)  # Hex → Decimal
    octal_num = oct(decimal_num)    # Decimal → Octal
    return octal_num[2:]  # Remove '0o' prefix

# Example
print(hex_to_oct("1F"))  # Output: 37 (1F₁₆ = 37₈)

# method 2
# using f-strings
hex_str = "1F"
octal_num = f"{int(hex_str, 16):o}"
print(octal_num)  # Output: 37

# method 3
# manual conversion (Hex ——› Binary ——› Octal)
def hex_to_oct(hex_str):
    # Hexadecimal → Binary (4 bits per hex digit)
    binary_str = bin(int(hex_str, 16))[2:]
    # Pad binary to make length divisible by 3
    binary_str = binary_str.zfill((len(binary_str) + 2) // 3 * 3)
    # Binary → Octal (3 bits per octal digit)
    octal_num = oct(int(binary_str, 2))[2:]
    return octal_num

# Example
print(hex_to_oct("1F"))  # Output: 37

