# 6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def square_list():
    list1=[]
    for i in range(1,31):
        list1.append(i**2)
    
    return list1[:5],list1[-5:]

first,last=square_list()
print ("First 5 Elements=",first)
print ("Last 5 Elements=",last)