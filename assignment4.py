#Assignment No 4:-
#Write a Python program to create a lambda function that adds 25
#to a given number passed in as an argument.

# def add25(num):
#     return num+25
# print("The added number is: ",add25(int(input("Enter Number: "))))


#By using lambda function

add25=lambda x: x+25
print("The added number is: ",add25(int(input('Enter Number: '))))
