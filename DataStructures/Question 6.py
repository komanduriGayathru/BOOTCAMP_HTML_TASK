# 6. 	Write a program in Python to iterate through 
# the list of numbers in the range of 1,100 and 
# print the number which is divisible by 3 and a multiple of 2.

x=list(range(1,101))   #range is always in () brackets whereas slice is done using []

print(x)
print(type(x))
lis=[]

for i in x:
    if i%3==0:
        lis.append(i)
print(lis)




