# 3.        Create a function that takes a list and returns a new list with unique
#  elements of the first list.

def unique_element(list1):
    unique_list=[] # I have taken a empty list and will append all the unique element in this.
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    print("The Unique Elements are: " ,unique_list)

unique_element([1,2,3,4,2,4,6,24,24,52,1,3])















