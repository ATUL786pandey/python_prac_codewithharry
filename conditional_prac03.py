'''
a spam comment is define as a text containg the following keyword 
"make a lot of money ","buy now ","subscribe  this ","click this "
write a program to detect this spam 

'''

#spam = ["make a lot of money ", "buy now", "subscribe this ", "click this "]


text =input("Enter the few  line sentence :")

if ("make a lot of money" in text) :
    spam = True
    
elif ("buy now" in text):
    spam=True
elif ("subscribe this " in text):
    spam= True
elif("click this " in text):
    spam=True
else:
    spam = False

if (spam ):
    print("these is spam message plaese ignor this ")
else:
    print ("this is not spam message ") 

