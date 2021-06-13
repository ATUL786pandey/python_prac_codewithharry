'''
can we have a set with 18(int) and 18(str) as a value in it .

'''
#a = {18,"18"}
a = set()
a.add(18)
a.add(18.0)
a.add("18")
print(a)
print(len(a))

 #Ans yes it can have bcoz there datatype is different 
