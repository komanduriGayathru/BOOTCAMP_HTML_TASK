# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” 
# and print the string which has even length of word.


def even_length_string(str):
    result=""
    for i in range(len(str)):   # it will go through the entire length of the string that is passed.
        if i%2==0:               # wherever the question of like this comes we have to go through the length of the string.
          result+=str[i]
    return result

print(even_length_string("hello my name is abcde"))

# sat="hello my name is abcde"
# print(len(sat))






