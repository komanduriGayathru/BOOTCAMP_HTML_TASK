#  1.   
def func(num):
    if num%3!=0 and num%7==0:
        return True
    else:
        return False
print(func(7))

# 2.

# normal method..............................
l=[1,2,3,4,5,6,7,8]
def func(l):
    for i in l:
        print(i*i)
func(l)

# by using map function.
mylist=[1,2,3,4,5,6,7,8]
def multiple(x):
    return x * x
   
print(list(map(multiple,mylist))) 


3
# normal method.....................
# str="Gayathri"
# for i in str:
#     if i.isupper():
#         print(i,end="")

# List Comprehension................
str="gayathri"
res=[i for i in str if i.isupper()]
print(res)



#  4.

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
d=(dict(zip(Student,capital)))
print(d)
print(type(d))








# 6.

def rev_str(name):
    for i in range (len(name) - 1, -1, -1):
        yield name[i]
for i in rev_str('Consultadd Training'):
    print(i ,end="")

    

#  7.

def my_decorator(func):
    def wrapper():
        print("I am in INDIA!!!")
        func()
        print("I came to USA!!!")
    return wrapper

def say_wee():
    print("Whee!!!")

x=my_decorator(say_wee)
x()





# 9.


print('Enter correct username and password to login!!!')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username=='satish' and password=='14':
        print('Access granted!!!')
        count += 1
        print(f"Congratulations!!! you have login in {count}st attempt")
        break
        
    else:
        print('Access denied. Try again!!!')
        count += 1
    print(f"your count is {count} !!! you have 3 attempt for login ")





