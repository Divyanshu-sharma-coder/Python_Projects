# Armstrong number checking programm

user_input = int(input("Enter a 3 digit Number : "))

num= user_input

a = num % 10 #unit digit
num = num // 10 
b = num % 10 #10th digit
c = num//10 #100th digit

armstrong = (a**3) + (b**3) + (c**3)

if armstrong == user_input:
  print("Number is Armstrong")
  
else:
  print("Not an Armstrong Number")
