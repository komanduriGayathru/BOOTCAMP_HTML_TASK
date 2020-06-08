# 8.        Define a function which can generate and 
# print a tuple where the value are square of numbers between 1 and 20.

def square():    # as awe are declaring the  range so there is no need to pass the parameters.
    l=list()    #as tuple do not have the append
    for i in range(1,21):
       l.append(i*2)
    print(tuple(l))

    print(type(tuple(l)))  # its giving the tuple as the type.

square()