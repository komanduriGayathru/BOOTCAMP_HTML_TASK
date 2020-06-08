# 6.          Define a function that can receive two integral numbers in string 
# form and compute their sum and print it in console.

# integral number are those who donot have fraction and all.
# eg: 3,6,5,7,8

def two_integral_numbers():
    num1=input("Enter first integral number : ")
    num2=input("Enter second integral number : ")
    # print(type(num1))
    # print(type(num2))
    
    res=int(num1)+int(num2)
    print(res)
two_integral_numbers()


