# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

ch=input("Enter your input:")
Letters=0
Digits=0
for i in range(0,len(ch)):
    if ((ord(ch[i])>=65 and ord(ch[i])<=90) or (ord(ch[i])>=97 and ord(ch[i])<=122)):
         Letters+=1
    elif (ord(ch[i])>=48 and ord(ch[i])<=57):
         Digits+=1

print ("Letters ",Letters)
print ("Digits ",Digits)
