# 13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 


import operator     #we need to import the operators
from functools import reduce    # and also reduce.

list = [[1, 2, 3], [4, 5], [6, 7, 8]]  # list given for us
print(type(list))
print(type(list[0]))  # that means there are list inside the lists.

joinlist = reduce(operator.add, list)  #reduce(fun,seq)  operator.add is a function 
print(joinlist)                        #The reduce() method reduces the list to a single value.


for i in joinlist:
    print(i,end="")



# a=4
# b=5
# print(operator.add(a,b)) #9

# # but what is string is to be added
# a1="satish"
# b1="gadge"
# print(operator.add(a1,b1)) #satishgadge

# #what if list is to be added
# a2=[1,2,3]
# b2=[4,5,6]
# print(operator.add(a2,b2)) #[1, 2, 3, 4, 5, 6]






