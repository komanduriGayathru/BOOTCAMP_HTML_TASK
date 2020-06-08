# 10. 	Write a program which can filter() to make a list
#  whose elements are even number between 1 and 20 ( both included)


number =[*range(1,21,1)]    # to amke the range work in list we have to add*
                           #so the third parameter helps to keep the gap  2 or 3 0r any number.
# print(number)

e = lambda x: x % 2 == 0  

# Example of lamda
# x = lambda a, b: a * b
# print(x(5, 6))


lis=list(filter(e, number))   # here list is define to make a list  filter(function, sequence)
print(lis)                     # here e it self i have assign to the functon lambda.
                               # where our function say to print even number from the sequesnce.















