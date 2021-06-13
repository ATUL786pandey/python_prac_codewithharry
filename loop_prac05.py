'''
write a program to find the sum of natural number 
'''
num=int(input("Enter the number "))
if num < 0:
    print("Enter the positive number ")

else:
    sum=0
    while num > 0:
        sum=sum +num
        num=num-1
    print("the sum of natural no is ",sum)