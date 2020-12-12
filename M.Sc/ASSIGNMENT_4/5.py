# Write a python code to take some string input. Now in the string find out how the
#frequency of each letter and print them along the letter alphabetically.

def main():
    freq = dict()
    s=input("Enter the string: ")
    for i in s: 
        if i in freq: 
            freq[i]+=1
        else: 
            freq[i]=1

    sort=sorted(freq.items(), key=lambda x:x[0])
    print("The output is:")
    print(sort)
    
main()
