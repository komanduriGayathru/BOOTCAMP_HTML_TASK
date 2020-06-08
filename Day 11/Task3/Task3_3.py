# 3. Write a program to get the sum and multiply of all the items in a given list.

list1=[1,2,3,4,5,6,7,8,9,10]
def multiply(mul_list):
    m=1
    for i in mul_list:
        m*=i
    return m


def sum(sum_list):
    s=0
    for i in sum_list:
        s+=i
    return s

m=multiply(list1)
print ("Multiplication of all elements of list=",m)

s=sum(list1)
print ("Sum of all elements of list=",s)
