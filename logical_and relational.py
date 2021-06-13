age = int(input("Enter the age  : "))

if age > 11  and  age < 18 :
    print("you are not eligible for voiting")

elif age > 18 and age <= 48:
    print("you are young age please select the valid candidate")
elif age >=49 and  age <=58:
    print("you are the experince person plaese select the right candidate")
elif age > 59:
    print ("your are senior citizen you are on priority")
else:
    print("you are child enjoy your life ")
