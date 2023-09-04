#Program to get length, maximum, and minimum of list
list=[6,5,3,6,34,5,3,2,4,654,5,3,543,987654567876543]
print("The list is", list)
print("1. Find the length of the list")
print("2. Find the maximum of the list")
print("3. Find the minimum of the list")
print("4. Exit the program")
while True:
    choice=int(input("Enter your choice"))
    if (choice==1):
        print("The length of the list is", len(list))
    elif (choice==2):
        print("The maximimum of your list is", max(list))
    elif (choice==3):
        print("The minimimum of your list is", min(list))
    elif (choice==4):
        break
    else:
        print("Your choice is not valid")
