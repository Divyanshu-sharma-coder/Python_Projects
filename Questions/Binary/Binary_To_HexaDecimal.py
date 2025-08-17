# Conversion on Binary into Hexadecimal

# method 1
# Using intermidiate Decimal Conversion

def binary_to_hex(binary_str):
    """
    Convert binary to hexadecimal by first converting to decimal then to hex
    """
    decimal_num = int(binary_str, 2)
    return hex(decimal_num)[2:]  # Remove '0x' prefix

# Example
print(binary_to_hex("11011010"))

# method 2
# direct conversion (python 3.10+)
def binary_to_hex(binary_str):
    """
    Direct conversion using f-string with binary input
    (Python 3.10+ feature)
    """
    return f"{int(binary_str, 2):x}"

# Example
print(binary_to_hex("11011010"))

#method 3
# using format function
def binary_to_hex(binary_str):
    """
    Convert binary to hex using format()
    """
    return format(int(binary_str, 2), 'x')

# Example
print(binary_to_hex("11011010"))

# method 4
# manual Conversion group by 4 bit manipulation
def binary_to_hex(binary_str):
    """
    Manual conversion by grouping binary digits into 4-bit nibbles
    """
    # Pad with leading zeros to make length multiple of 4
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
        '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'
    }
    
    hex_str = []
    for i in range(0, len(padded), 4):
        nibble = padded[i:i+4]
        hex_str.append(hex_map[nibble])
    
    return ''.join(hex_str)

# Example
print(binary_to_hex("11011010"))

# method 5

# using Bit manipulation
def binary_to_hex(binary_str):
    """
    Convert binary to hex using bit manipulation
    """
    num = int(binary_str, 2)
    hex_digits = []
    
    if num == 0:
        return '0'
    
    while num > 0:
        digit = num & 0xf  # Get last 4 bits
        hex_digits.append(f"{digit:x}")
        num >>= 4  # Shift right by 4 bits
    
    return ''.join(reversed(hex_digits))

# Example
print(binary_to_hex("11011010"))

# method 6
# Handling Different cases
def binary_to_hex(binary_str, uppercase=False):
    """
    Convert binary to hex with uppercase option
    """
    hex_str = hex(int(binary_str, 2))[2:]
    return hex_str.upper() if uppercase else hex_str

# Example
print(binary_to_hex("11011010", True))
