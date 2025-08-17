# Write a program that takes a list from user and give a new list of all square no. present in that list

li_1 = list(map(int, input("Enter No. Separated by spaces: ").split()))
print(f"The Original list is : {li_1}")

li_2 = [x**2 for x in li_1]
print("The Square Of No. are:", li_2)
