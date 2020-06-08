# 9. Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

dic1={}

def dict_square(n):
    for i in range(1,n+1):
        dic1[i]=i*i
    return dic1

a=dict_square(5)
print (a)