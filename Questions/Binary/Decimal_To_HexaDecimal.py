
# Converting Decimal Into Hexa Decimal
def decimal_to_hex(decimal_num):
    """
    Convert decimal to hexadecimal using hex() function.
    Returns a string without the 0x prefix.
    """
    return hex(decimal_num)[2:]

# Example usage
try:
    decimal_number_str = input("Enter Your Decimal Digit: ")
    decimal_number = int(decimal_number_str)  # Convert input string to an integer
    hex_number = decimal_to_hex(decimal_number)
    print(f"Decimal {decimal_number} is hexadecimal {hex_number}")
except ValueError:
    print("Invalid input. Please enter a valid decimal number.")


#2nd Method

# using String Formatting
def decimal_to_hex(decimal_num):
    """
    Convert decimal to hex using string formatting.
    """
    return "{0:x}".format(decimal_num)

# Example usage
print(decimal_to_hex(255)) 

#3rd Method
# Manual Conversion

def decimal_to_hex(decimal_num):
    """
    Convert decimal to hexadecimal using division by 16 method.
    Handles 0 and positive integers.
    """
    if decimal_num == 0:
        return "0"
    
    hex_digits = "0123456789abcdef"
    hex_str = ""
    num = decimal_num
    
    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num = num // 16
    
    return hex_str

# Example usage
print(decimal_to_hex(255)) 


#method 4 
# Using F-string(python 3.6+)
def decimal_to_hex(decimal_num):
    """
    Convert decimal to hex using f-strings.
    """
    return f"{decimal_num:x}"

# Example usage
print(decimal_to_hex(255))  # Output: ff

#method 5
#using Format() function
def decimal_to_hex(decimal_num):
    """
    Convert decimal to hex using format() function.
    """
    return format(decimal_num, 'x')

# Example usage
print(decimal_to_hex(255)) 

#method 6
#Handling Negative Numbers
def decimal_to_hex(decimal_num):
    """
    Convert decimal to hex with proper negative number handling.
    Returns 2's complement for negative numbers.
    """
    if decimal_num >= 0:
        return f"{decimal_num:x}"
    else:
        # For negative numbers, Python's hex() shows 2's complement
        return hex(decimal_num & 0xffffffff)[2:]

# Example usage
print(decimal_to_hex(-255))  
