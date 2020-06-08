# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 

predefined=[2,3,45,5,6,7,8,9,10]

def odd_list(list1):
    odd=[]
    for i in list1:
        if(i%2!=0):
            odd.append(i)
    return odd

New_list=odd_list(predefined)
print ("New list=",New_list)