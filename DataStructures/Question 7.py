# 7. 	Write a program in Python to reverse a string and
#  print only the vowel alphabet if exist in the string with their index.


user=input("Enter any string of your choice ?? ")

lis=[]
for i in user:
    if i in "aeiouAEIOU":
        lis.append(i)
   

print(lis)




