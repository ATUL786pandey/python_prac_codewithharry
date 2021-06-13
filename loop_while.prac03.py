'''
write a program tomprint a table using while loop 

'''
num=int(input("Enter a number to print a table: "))
i=1
while i<=10:
    print(f"{num}x{i} = ",(num*i))
    i=i+1
print (f"table for {num} is printed")