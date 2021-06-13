'''
write a program to print a table using for loop in reverse order
'''
num=int(input("Enter the number "))
for i in range (10,0,-1):
    print(f"{num} x {i} =",(num*i))
