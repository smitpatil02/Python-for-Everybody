# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
list=[]

while True:
    try:
        x = input("Enter the numbers")
        num = int(x)
        list.append(num)
    except:
        if x == "done":
            break
        else:
            print("Invalid input")

for value in list:
    if largest is None:
    	largest = value
    elif largest<value:
        largest = value

print("Maximum is",largest)

for value in list:
    if smallest is None:
    	smallest = value
    elif smallest>value:
        smallest = value

print("Minimum is",smallest)
