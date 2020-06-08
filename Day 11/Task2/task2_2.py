# Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition 
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
# At the end if the answer of any operation is Negative print a statement saying “zsa”
# Note: At a time user can perform one action at a time.

import operator as op
op_dict={"1":op.add,"2":op.sub,"3":op.truediv,"4":op.mul}

x=input("Enter any of the following Options:\n 1-Addition \n 2-Subtraction \n 3-Divison \n 4-Multiplication\n 5-Average")
if (x in op_dict):
    first=input("Enter first number:")
    second=input("Enter second number:")
    y=op_dict.get(x)
    result=y(int(first),int(second))
    if(result<0):
        print("zsa")

elif(int(x)==5):
    first1=input("Enter first number:")
    second2=input("Enter Second number:")
    result=(int(first1)+int(second2))/2
    if(result<0):
        print("zsa")
