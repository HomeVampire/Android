# Write a python code to draw the pascle triangle
#                           1
#                          1 1
#                         1 2 1
#                        1 3 3 1
#                       1 4 6 4 1

def main():
    n=int(input("Enter depth of the pattern: "))
    coef=1
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(i+1):
            if j==0 or i==0:
                coef=1
            else:
                coef=int(coef*(i-j+1)/j)
            print(coef,end=" ")
        print("")
    
main()
