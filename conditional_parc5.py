'''
write a program which find out weather a given name is present in the list or not
'''

names =["Atul","puja","sanjay","reena","nirmala","Gritisha"]

name = input("Enter the name to check  : ")

if name in names:
    print(f"{name} is present in this list ")
else:
    print(f"{name} is not present in the list")