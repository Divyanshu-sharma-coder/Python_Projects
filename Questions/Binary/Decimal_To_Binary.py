#Converting Decimal Into Binary

#method 1

def decimal_to_binary(decimal_num):
    
   # Convert a decimal number to binary #using Python's built-in bin() function.
    #Returns a string without the '0b' prefix.
    
    return bin(decimal_num)[2:]

# Example usage
decimal_number = int(input("Enter The Decimal Digit : "))
binary_number = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} is binary {binary_number}")  
    
   
    
# 2nd Method
def decimal_to_binary(decimal_num):
    
   # Convert decimal to binary using string formatting.
    
    return "{0:b}".format(decimal_num)

a = int(input("Enter the Decimal Digit : "))
print(decimal_to_binary(a))  


# 3rd Method
# Manual Conversion Algo.

def decimal_to_binary(decimal_num):
    
    #Convert decimal to binary using division by 2 method.
    #Handles 0 and positive integers.
    
    if decimal_num == 0:
        return "0"
    
    binary_str = ""
    num = decimal_num
    
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    
    return binary_str

b = int(input("Enter Your Decimal Digit : "))
print(decimal_to_binary(b)) 

 
  # method 4 
  # Using F-strings python 3.6+
def decimal_to_binary(decimal_num):
    
    #Convert decimal to binary using f-strings.
    
    return f"{decimal_num:b}"

c = int(input("Enter The Decimal Digit : "))
print(decimal_to_binary(c))  


# 5th Method 
# Recursvive Approach

def decimal_to_binary(decimal_num):
   
   # Recursive decimal to binary conversion.
    
    if decimal_num <= 1:
        return str(decimal_num)
    else:
        return decimal_to_binary(decimal_num // 2) + str(decimal_num % 2)

num = int(input("Enter Decimal Digit : "))
print(decimal_to_binary(num))  
