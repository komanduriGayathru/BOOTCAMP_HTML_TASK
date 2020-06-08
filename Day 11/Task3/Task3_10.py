# 10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

sequence=input("Enter your Sequence:")

def list_and_tuples(string1):
    list=string1.split(",")
    tuple_list=tuple(list)
    return list,tuple_list

result_list,result_tuple=list_and_tuples(sequence)
print("List=",result_list)
print("Tuple=",result_tuple)