# Range function in python generates a range of items. It looks like range( start(optional),
# end, step (optional)). Using this function we have already printed 1 to 10. Now
# write a python code to print all the number divided by 3 between 1 to 100.

def main():
    print("The numbers devide by 3 are: ")
    for i in range(1,100):
        if i%3==0:
            print("[",i,"],",end=" ")
    
main()
