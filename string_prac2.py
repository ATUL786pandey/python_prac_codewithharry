'''
write a program to fill in a  letter template given below  with name and date 
letter= <|Name>  you are selected <|Date>

'''

name = input("Enter your name : ")
date = input("Enter date : ")
letter= "<|Name> \n you are selected on \n <|Date>"
letter = letter.replace("<|Name>",name)
letter = letter.replace("<|Date>",date)
print(letter)