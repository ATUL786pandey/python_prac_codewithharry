'''
write a program to find out weather a student is pass or fail ,if it require 40 % and atleast 33%
in each subject and the mark are taken as input by the user   
'''

sub1 = int(input("Enter the maths mark : "))
sub2 = int(input("Enter English mark : "))
sub3 = int(input("Enter Science mark : "))

if (sub1 <33 or sub2< 33 or sub3 < 33):
    print("you are fail you have score less than 33 marks  ")
elif (sub1+sub2+sub3)/3 < 40:
    print("you are fail due to your percentage is less than 40")
else :
    print("congratulation you are pass")