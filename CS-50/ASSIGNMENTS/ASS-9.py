def mean(list1): ## MEAN METHOD
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]  
    return sum/len(list1)

def deviation(list1): ## DEVIATION METHOD
    means=mean(list1)
    n=len(list1)
    deviation=0
    for i in range(n):
        deviation+=(list1[i]-means)*(list1[i]-means)   
    return deviation

def cross_product(list1, list2): ## CROSS PRODUCT OF X AND Y
    means1=mean(list1)
    means2=mean(list2)
    sum_of_cross_product=0
    for i in range(len(list1)):
        sum_of_cross_product+=(list1[i]-means1)*(list2[i]-means2)
    return sum_of_cross_product

def corelation_coefficient(deviation_x, deviation_y, xy):
    import math
    xx=math.sqrt(deviation_x)
    yy=math.sqrt(deviation_y)

    r=xy/(xx*yy)
    print("The value of Pearson's Correlation Coefficient=",r)


def main():
    list1=list()
    n=int(input("Enter total No. of entries"))
    for i in range(n):
        list1.append(int(input("Enter The elements")))
    print("The values of X:", list1)

    list2=list()
    for i in range(n):
        list2.append(int(input("Enter The elements")))
    print("The values of Y:", list2)

    deviation_x = deviation(list1)
    deviation_y = deviation(list2)

    xy=cross_product(list1,list2)

    corelation_coefficient(deviation_x, deviation_y, xy)

main()