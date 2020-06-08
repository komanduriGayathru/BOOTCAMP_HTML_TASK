# 8.	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}

def concatenate(dic1,dic2):
    return dic1.update(dic2)

result=concatenate(a,b)
print (a)