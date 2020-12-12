def sort(list1): ## SORTING METHOD
    n=len(list1)   
    for i in range(n):
        maximum=list1[0]
        index=0
        for j in range(n):
            if maximum<list1[j]:
                maximum=list1[j]
                index=j
        temp=list1[n-1]
        list1[n-1]=list1[index]
        list1[index]=temp
        n=n-1
    return list1

def mean(list1): ## MEAN METHOD
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]  
    return sum/len(list1)

def median(list1): ## MEDIAN METHOD
    n=len(list1)
    list2=list()
    list2=sort(list1)
    list2=list1
    if n%2 != 0:
        print("MEDIAN=",list1[int(n/2)])
    else:
        sum_of_mids=list1[int(n/2)-1]+list1[int(n/2)]
        print("MEDIAN=",sum_of_mids/2)

def mode(list1): ## MODE METHOD
    n=len(list1)
    maximum=max(list1)
    maximum+=1
    counts=[0]*maximum
    for i in range(n):
        counts[list1[i]]+=1
    occurence=max(counts)
    if occurence == 1:
        print("ALL ELEMENTS ARE UNIQUE")
    else:
        for i in range(maximum):
            if counts[i] == occurence:
                print("MODE=",i)

def ranges(list1): ## RANGE METHOD
    minimum=min(list1)
    maximum=max(list1)
    print("RANGE=",maximum-minimum)

def variance(list1): ## VARIANCE METHOD
    means=mean(list1)
    n=len(list1)
    variance=0
    for i in range(n):
        variance+=(list1[i]-means)*(list1[i]-means)   
    return variance/n

def standard_daviation(list1): ## STANDARD DAVIATION
    variances=variance(list1)
    import math
    standard_daviation=math.sqrt(variances)
    print("STANDARD DAVIATION=",standard_daviation)


def main():
    list1=list()
    n=int(input("Enter total No. of entries"))
    for i in range(n):
        list1.append(int(input("Enter The elements")))
    print("The list is:", list1)
    means=mean(list1)
    print("MEAN=",means)
    median(list1)
    mode(list1)
    ranges(list1)
    variances=variance(list1)
    print("VARIANCE",variances)
    standard_daviation(list1)

main()