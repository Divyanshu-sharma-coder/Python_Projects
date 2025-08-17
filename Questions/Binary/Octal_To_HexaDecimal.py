# Conversion of Octal into HexaDecimal

# method 1 
# using int and hex 

def oct_to_hex(oct_str):
    decimal_num = int(oct_str, 8)  # Octal → Decimal
    hex_num = hex(decimal_num)     # Decimal → Hex
    return hex_num[2:]  # Remove '0x' prefix

# Example
print(oct_to_hex("37"))  # Output: 1f (37₈ = 1F₁₆)

# method 2
# using f-strings

oct_str = "37"
hex_num = f"{int(oct_str, 8):x}"
print(hex_num)  # Output: 1F

# method 3
# using manual conversion (Hex ——› Binary ——› Octal)
def oct_to_hex(oct_str):
    # Octal → Binary (3 bits per octal digit)
    binary_str = bin(int(oct_str, 8))[2:]
    # Pad binary to make length divisible by 4
    binary_str = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    # Binary → Hex (4 bits per hex digit)
    hex_num = hex(int(binary_str, 2))[2:]
    return hex_num

# Example
print(oct_to_hex("37"))  # Output: 1f
