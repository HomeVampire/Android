def avarage(a,n):
    sum=0

    for i in range(n):
        element=int(input("Enter the element: "))
        a.append(element)
        sum=sum+a[i]

    print("The sum is: ",sum)
    return sum/n

def main():
    n=int(input("Enter the number of elements to be inserted: "))
    a=[]
    avg=avarage(a,n)
    print("The avarage is: ",avg)

main()