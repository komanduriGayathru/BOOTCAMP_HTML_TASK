# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower():
    uppercase=0
    lowercase=0
    user_input=input("Enter any string with both the uppercase and lowercase characters: ")
    for c in user_input:
        if c.isupper():
            uppercase+=1
        elif c.islower():
            lowercase+=1
        else :
            pass
    print("No. of Upper case characters :", uppercase )
    print("No. of Lower case Characters :", lowercase)

upper_lower()







