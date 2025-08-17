# Conversion of Binary into Octal

# method 1 Using int and oct built in functions
def binary_to_octal(binary_str):
    decimal_num = int(binary_str, 2)  # Binary → Decimal
    octal_num = oct(decimal_num)      # Decimal → Octal
    return octal_num[2:]  # Remove '0o' prefix

# Example
print(binary_to_octal("101010"))  # Output: 52 (since 101010₂ = 52₈)

# method 2 
# 1. Using F-string
binary_str = "101010"
octal_num = f"{int(binary_str, 2):o}"
print(octal_num)  # Output: 52
#2. Using Format() functions
binary_str = "101010"
octal_num = format(int(binary_str, 2), 'o')
print(octal_num)  # Output: 52


# method 3
# manual Conversion (Grouping By 3 Bit Manipulation)

def binary_to_octal(binary_str):
    # Pad with leading zeros to make length divisible by 3
    padded = binary_str.zfill((len(binary_str) + 2) // 3 * 3)
    
    # Binary → Octal mapping (3-bit groups)
    octal_map = {
        "000": "0", "001": "1", "010": "2", "011": "3",
        "100": "4", "101": "5", "110": "6", "111": "7"
    }
    
    octal_digits = []
    for i in range(0, len(padded), 3):
        group = padded[i:i+3]
        octal_digits.append(octal_map[group])
    
    return ''.join(octal_digits)

# Example
print(binary_to_octal("101010"))  # Output: 52
