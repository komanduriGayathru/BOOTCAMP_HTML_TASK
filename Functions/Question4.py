# 4.         Write a program that accepts a hyphen-separated sequence of words
#  as input and prints the words in a hyphen-separated
#   sequence after sorting them alphabetically.

#ans-hef-dfee-ad =sort this alphabetically with the hipen saperated.

user=input("Enter the name : ")

names=[i for i in user.split("-")]
names.sort()
print("-".join(names))






