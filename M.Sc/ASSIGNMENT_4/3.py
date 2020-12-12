# Write a python code to make a list of all prime numbers between 1 to 1000.

def main():
    output=list()
    print("The prime numbers are: ")
    output.append(1)
    output.append(2)
    for i in range(3,1000):
        flag=0
        for j in range(2,int(i/2)+1):
            if i%j==0:
                flag=1
                break
        if flag==0:
            output.append(i)

    print(output)
    
main()
