'''
write aprogram to create a dictionary of hindi word with values as their english translation
provide user with an option to look it up
'''

mydict = {
    "pankkha":"fan",
    "gadi": "Watch",
    "pustak" : "book",
    "kalam" : "pen",
    "bhojan" : "Dinner"

}
print("choose the below  word to translate in english \n",mydict.keys())

a=input("Enter the choice from above option : ")
if a in mydict:

    print(mydict.get(a))
    print("thank you")
else :
    print(" the  word is invalid word")
   
    

