user = int(input("Enter No. Of Rows : "))
if user <= 0:
  print("Please Enter a valid Number !! ")
else:
  num = 1
  for user in range (1 , user + 1):
    for column in range (user):
      print(num , end = " ")
      num = num + 1
      
    print()
