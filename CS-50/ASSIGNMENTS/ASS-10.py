def main():
    n=int(input("Enter Total number of elements:"))
    a=[]
    for j in range(n):
        element=int(input("Enter the Element: "))
        a.append(element)

    for i in range(n):
        if a[i]%3==0:
            print("FIZZ", end="")
        elif a[i]%5==0:
            print("BUZZ")
        ##elif a[i]%5==0 and a[i]%3==0:
            ##print("FIZZ BUZZ")
        else:
            pass

main()
        