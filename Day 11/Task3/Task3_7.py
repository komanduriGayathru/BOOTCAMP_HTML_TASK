# Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

sample_list=[[1,3,5,7,9,10],[2,4,6,8]]
def replace_last(list1):
    list1[0].pop()
    for i in list1[1]:
        list1[0].append(i)
    list1.pop()
    return list1

ans=replace_last(sample_list)
print (ans)