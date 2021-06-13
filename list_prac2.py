# write a program to accept the mark of six student and display them in sorted order
mark1 = input("Enter the  first mark : ")
mark2 = input("Enter the  second mark : ")
mark3 = input("Enter the  third mark : ")
mark4 = input("Enter the  fourth mark : ")
mark5 = input("Enter the  fifth mark : ")
mark6 = input("Enter the  sixth mark : ")

marks = []
marks.append(mark1)
marks.append(mark2)
marks.append(mark3)
marks.append(mark4)
marks.append(mark5)
marks.append(mark6)

marks.sort()
print(marks)