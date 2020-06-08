#Write a program to complete the task given below:
#Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
#Use z for adding 30 into it and print the final result by using variable result.

x=input("Enter first number between 1 to 10:")
y=input("Enter second number between 1 to 10:")
while(True):
    if ((int(x)>=1 and int(x)<=10) and (int(y)>=1 and int(y)<=10)):
        z=int(x)+int(y)+30
        print("final result=",z)
        break
    else:
        print("One or more invalid numbers. Enter numbers again")
        x=input("Enter first number between 1 to 10:")
        y=input("Enter second number between 1 to 10:")