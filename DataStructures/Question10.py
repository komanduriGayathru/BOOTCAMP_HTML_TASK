# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number
#  is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list 
# and return the maximum out of the list.



def even_odd(user):
    even_list=[]
    odd_list=[]
    for i in user:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(even_list)
    print(odd_list)
even_odd([2, 5, 13, 17, 51, 62, 73, 84, 95] ) 