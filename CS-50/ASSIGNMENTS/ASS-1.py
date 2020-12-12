print("Enter 1st number:")
a = int(input())
print("Enter 2nd number:")
b = int(input())


def maximum(a, b):
    if a > b:
        print("The Max Number is:")
        print(a)
    elif a < b:
        print("The Max Number is:")
        print(b)
    else:
        print("Both numbers are Same")


maximum(a, b)
