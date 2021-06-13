'''
write a program tofind the graetest of four number enter by the user 

'''

num = int(input("Enter the first no : "))
num1 = int(input("Enter the Second no : "))
num2 = int(input("Enter the third no : "))
num3 = int(input("Enter the fourth no : "))

if num > num1:
    f1= num 
else:
    f1= num1 

if num2 > num3:
    f2 = num2 
else:
    f2= num3 

if (f1 > f2):
    print(f"the {f1} is greater")
else:
    print(f"the {f2} is greater ")