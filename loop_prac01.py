'''
write a program to print multiplication of table using for loop
'''
num =int(input("Enter a  number to print a table:  "))
for i in range (1,11):
    print(f"{num} x {i} =",(num*i))
print("table is finish ")