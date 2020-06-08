#Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “c” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

number=15;
if (number%5==0 and number%3==0):
    print ("Consultadd Python Training")
elif(number%5==0):
    print("c")
elif(number%3==0):
    print("Consultadd")
