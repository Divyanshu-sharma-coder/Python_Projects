# Coverting Decimal into octal
# method 1 using built in function
def decimal_to_octal(decimal_num):
    """Converts decimal to octal using Python's built-in oct()"""
    return oct(decimal_num)[2:]  # Remove '0o' prefix

# Example
print(decimal_to_octal(78))  # Output: 116

#method 2
# using String Formatting
def decimal_to_octal(decimal_num):
    """Converts decimal to octal using string formatting"""
    return "{0:o}".format(decimal_num)

# Example
print(decimal_to_octal(78)) 

# method 3
# using format function
def decimal_to_octal(decimal_num):
    """Converts decimal to octal using format()"""
    return format(decimal_num, 'o')

# Example
print(decimal_to_octal(78))  
# method 4
# using f-strings (python 3.6+)
def decimal_to_octal(decimal_num):
    """Converts decimal to octal using f-strings"""
    return f"{decimal_num:o}"

# Example
print(decimal_to_octal(78))

# method 5
# manual conversion (divison by 8)
def decimal_to_octal(decimal_num):
    """Manually converts decimal to octal using division by 8"""
    if decimal_num == 0:
        return "0"
    
    octal_digits = []
    num = decimal_num
    
    while num > 0:
        remainder = num % 8
        octal_digits.append(str(remainder))
        num = num // 8
    
    return ''.join(reversed(octal_digits))

# Example
print(decimal_to_octal(78))

# method 6
# Recursive Approach
def decimal_to_octal(decimal_num):
    """Recursively converts decimal to octal"""
    if decimal_num < 8:
        return str(decimal_num)
    else:
        return decimal_to_octal(decimal_num // 8) + str(decimal_num % 8)

# Example
print(decimal_to_octal(78))

# method 7
# Handling Missing values
def decimal_to_octal(decimal_num):
    """Handles negative numbers (returns 2's complement)"""
    if decimal_num >= 0:
        return oct(decimal_num)[2:]
    else:
        return oct(decimal_num & 0xFFFFFFFF)[2:]  # 32-bit representation

# Example
print(decimal_to_octal(-78))
