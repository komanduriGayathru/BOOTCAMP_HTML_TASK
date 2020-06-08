#Swap two numbers using the third variable as the result name and do the same
#task without using any third variable

#Subtask 3

#Subtask 3 part 1
x=10;y=20;result=30
print ("Method 1: Before: x=",x," y=",y)
result=x
x=y
y=result
print ("Method 1: After: x=",x," y=",y)

#Subtask 3 part 2
x=14; y=34
print ("Method 2: Before: x=",x," y=",y)
x+=y
y=x-y
x=x-y
print ("Method 2: After: x=",x," y=",y)
