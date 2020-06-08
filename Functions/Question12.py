# 12. 	Write a function to compute 5/0 and use try/except to 
# catch the exceptions

def try_catch():
    try:
        x=(5/0)  # as we know that when a number is divided by 0 it gives an error
        print(x)
    except:
        print("Error dividing with zero!!!")
try_catch()








