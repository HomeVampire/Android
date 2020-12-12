# Write a python code to draw the following pattern
#                        *
#                        **
#                        ***
#                        ****

def main():
    n=int(input("Enter depth of the pattern: "))

    for i in range(1,n+1):
        print("*"*i)
main()
