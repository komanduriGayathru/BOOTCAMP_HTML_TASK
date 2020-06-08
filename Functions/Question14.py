#  14. 		
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

# OutPut:2

# A finally clause is always executed before leaving the try statement, 
# whether an exception has occurred or not. When an exception has occurred 
# in the try clause and has not been handled by an except clause 
#  it is re-raised after the finally clause has been executed

#  def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()

# it will give an error as the f(x,4) is just called but not defined anywhere.


