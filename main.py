#This program employs the linear search algorithm to find elements in polynomial time(O(n))
from array import *
def linear_search(data,target):
    for y in range(len(data)):
        if data[y]==target:
            print(target," found at index ",y," of the array")
            return
    print(target," not found in the array")

data_array=array('i',[])
size=int(input("How many values do you want to input"))
print("Input the values")
for i in range(0,size,1):
    data_array.append(int(input()))
element=int(input("Input element to be searched for"))
linear_search(data_array,element)
