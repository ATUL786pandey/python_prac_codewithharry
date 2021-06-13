'''
write a program to print a rectangle shape patter
* * * * * * * 
*           *
*           *
*           *
* * * * * * *
like this 
'''

row=int(input("enter the no of row : "))
col=row+2
for i in range (0,row):
    for j in range (0,col):
        if i==0 or i==(row-1) or j==0 or j==(col-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# write a program to print a sqaure shape pattern


row=int(input("Enter the no of row : "))
col=row
for i in range (row):
    for j in range (col):
        if i==0 or i==(row-1) or j==0 or j==(col-1):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()
    