# 7.        Define a function that can accept two strings as input and 
# print the string with maximum length in console. If two strings have the same length, 
# then the function should print all strings line by line.

def two_string():
    str1=input("Enter first string: ")
    str2=input("Enter second string: ")

    if len(str1) > len(str2):
        print("The string with maximum length is :",str1)
    else:
        print("The string with maximum length is :",str2)

    print("The first string is: ",str1)
    print("The second string is: ",str2)



two_string()
