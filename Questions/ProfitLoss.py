
# Programm to find profit and loss

cp = float(input("Enter your Cost Price : "))
sp = float(input("Enter your Sell Price : "))

if cp > sp:
  amount = cp - sp
  print(f"You are in loss and loss amount is : {amount}")
else:
  amount2 = sp-cp
  print(f"You are in Profit and profit amount is : {amount2}")
