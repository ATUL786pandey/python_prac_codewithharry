'''
write a program to print a star patter in right angle triangle shape 
'''

num=int(input("Enter the no row want to print : "))

for i in range (1,num+1):
    for j in range (i):
        print("*",end=" ")
    print()
    
#write a program to print right angle triangle in reverse order

a=int(input("Enter the no of rows : "))
for i in range (a,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()