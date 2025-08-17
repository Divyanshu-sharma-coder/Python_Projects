def binary_to_decimal(binary_str):
    """
    Convert a binary string to its decimal equivalent.
    
    Args:
        binary_str (str): A string representing a binary number (e.g., '1010')
    
    Returns:
        int: The decimal equivalent of the binary number
    """
    decimal = 0
    length = len(binary_str)
    
    for i in range(length):
        # Get the current digit (starting from left)
        digit = int(binary_str[i])
        # Calculate its value (digit * 2^position)
        decimal += digit * (2 ** (length - 1 - i))
    
    return decimal

# Example usage
binary_number = str(input("Enter Binary Number to convert it into Decimal : "))
decimal_number = binary_to_decimal(binary_number)
print(f"Binary {binary_number} is decimal {decimal_number}")

# You can use built in int function like this also
binary_str = "1101"
decimal_num = int(binary_str, 2)
print(decimal_num)  # Output: 13

# You can use bit manipulation like this
def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = (decimal << 1) | int(digit)
    return decimal
    
    
# You can use list comprehension method like this 
def binary_to_decimal(binary_str):
    return sum(int(digit) * (2 ** i) for i, digit in enumerate(reversed(binary_str)))
