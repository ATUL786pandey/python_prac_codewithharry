'''
write a program to print the star pattern in triangle shape 
'''
num=int(input("Enter the no of rows to print : "))

for i in range (0,num):
    for j in range (0,num-i-1):
        print(end=" ")
    for j in range (0,i+1):
        print("*",end=" ")
    print()
    

# write a program to print a pyramid in the reverse order

a=int(input("Enter the no row : "))

for i in range (a,0,-1):
    for j in range (a-i):
        print(end=" ")
    for j in range (0,i):
        print("*",end=" ")
    print()


