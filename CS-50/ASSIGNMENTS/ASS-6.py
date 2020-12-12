n=int(input("Enter the number of elements to be inserted: "))
a=[]
rev=[]
for i in range(n):
    element=input("Enter the element: ")
    a.append(element)

rev=[]
rev=a[n::-1]##Slicing
if rev==a:
    print("The String is Palindrome")
else:
    print("The String is Not-Palindrome")

