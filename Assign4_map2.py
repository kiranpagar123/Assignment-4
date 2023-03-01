# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]


def square(lst):
    return lst**2
length=int(input("Enter length: "))
lst=[]
for i in range(length):
    numbers=int(input("Enter Elements: "))
    lst.append(numbers) 
print("Square the elements of the list is: ",list(map(square,lst))) 


