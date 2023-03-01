# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]


def triple(lst):
    return lst*3
length=int(input("Enter the length: "))
lst=[]
for i in range(length):
    element=int(input("Enter the numbers: "))
    lst.append(element)
print("Triple of list numbers is: ",list(map(triple,lst)))

