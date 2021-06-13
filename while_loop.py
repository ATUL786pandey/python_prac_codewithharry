'''
the synatax for while loop is 
while(condition):
    statement

'''
#example for while loop is 
#program to print the value of i till the  given range 



i=1
while i <=10:
    print("yes",str(i))
    i=i+1
print("process done ")



# program to print table of the given number by the user 
num=int(input("Enter the number : "))
i=1
while i <=10:
    print(f"{num} x {i} = ",(num *i))
    i=i+1
print(f"the table of {num} is done ")



#program to print name in alphabetical squence  order 
name ="Atul"
i=0
while i<len(name):
    print(name[i])
    i=i+1
print("done ")
