'''
write a progarm tocalculate the factorial of a number using for loop
'''
#factorial using while loop

num=int(input("Enter the number : "))
fact=1
while num > 0:
    fact=fact*num
    num=num-1
print(fact)

#factorail using for loop

num=int(input("Enter the number : "))
fact=1
for i in range (num,1,-1):
    fact=fact*i
print (fact)