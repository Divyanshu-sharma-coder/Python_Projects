# User gives a list and in return it gets a list of evem numbers 

def even_numbers(li):
  # Corrected: iterating over 'li' and using 'num' consistently
  return [num for num in li if num % 2 == 0]

# Corrected: converting map object to a list
li = list(map(int, input("Enter Numbers : ").split()))
print(even_numbers(li))
