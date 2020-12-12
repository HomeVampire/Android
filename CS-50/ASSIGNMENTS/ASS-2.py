print("Enter 1st number:")
a=int(input())
print("Enter 2nd number:")
b=int(input())
print("Enter 3rd number:")
c=int(input())

def add(a, b, c):
    d=a+b+c
    print("The Sum is:")
    print(d)

def multi(a, b, c):
    d=a*b*c
    print("The Value of Multiplication is:")
    print(d)

add(a, b, c)
multi(a, b, c)

print("(6t^3 + 1)^3 - (6t^3 - 1)^3 - (6t^2)^3")
print("To find the value of the equation enter value for t")
t=int(input())

def eq(t):
    temp=pow((6*pow(t,3)+1),3) - pow((6*pow(t,3)-1),3) - pow((6*pow(t,2)),3)
    print("The Result is:")
    print(temp)

eq(t)