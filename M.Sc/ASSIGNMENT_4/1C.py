# Write a python code to draw the following pattern
#                           *
#                          ***
#                         *****
#                        *******

def main():
    n=int(input("Enter depth of the pattern: "))
    n=(n*2)-1
    for i in range(1,n+1,2):
        s=int((n-i)/2)
        print(" "*s,"*"*i)
    
main()
