    # 11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement.
    #  Example: 12abcbacbaba344ab  
    #  Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

user=input("Enter any string that holdes character as well as the numbers : ")

# user = 'it was the best of times it was the worst of times '

wordfreq = []   # created a empty list.
for w in user:
    wordfreq.append(user.count(w))  #The count() method returns the number of elements with the specified value.

print((list(zip(user, wordfreq))))


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)

#output:



#(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))