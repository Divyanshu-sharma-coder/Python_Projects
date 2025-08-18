# Programm for printing Calander

import calendar
while True:
  year = input("Enter Which Year you want to See or type exit to quit : ")
  month = input("Enter the Specific Month of that Year or type exit to quit : ")
  if year.lower() == "exit" or month.lower() == "exit":
    print("Thank you for using !! ")
    break
  try:
    year = int(year)
    month = int(month)
  except ValueError:
    print("Invalud Month and Year !! ")
    continue
  if month < 1 or month > 12:
    print("Please Choose Valid Month !! ")
    continue
  if year < 1:
    print("Invalid Year !!")
    continue
  print(calendar.month(year,month))
