# 3. 	Create a list of given structure and run 
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]  
print(type(x))  # it is a list.

#Access list [1, 2, 3, 4]
print(x[5][:4])

# Access list [600,  700]
print(x[6:8])   # slicing

# Access list [100, 300, 500, 600, 800]
print(x[::2])  # i can even start with the 0 which is equal to the blank space.

# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[: : -1])

# Access list [10]
print(x[5][5][0])    # beautiful!!! example

# Access list [ ]
print(x[:]) # means the complete list.



