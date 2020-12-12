##IMPORT AN CSV FILE
def csv():
    import csv
    dataset=list()
    with open('C:\WORK\PROGRAM\PYTHON\CS-50\DATASETS\dataset.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            dataset.append(line)
    return dataset
############################################################################
def minimum(a):
    mini=int(a[0])
    for i in range(1,len(a)):
        if mini>int(a[i]):
            mini=int(a[i])
    return mini

def maximum(a):
    maxi=int(a[0])
    for i in range(1,len(a)):
        if maxi<int(a[i]):
            maxi=int(a[i])
    return maxi

def min_max_votes(dataset):
    for i in range(1,len(dataset)):
        print(dataset[i][0])
        a=dataset[i][1:]
        minpos = 1+ a.index(str(minimum(a)))
        maxpos = 1+ a.index(str(maximum(a)))

        print("Got minimum vote in: ",dataset[0][minpos])
        print("Got maximum vote in: ",dataset[0][maxpos])
##########################################################################
def total_votes(dataset):
    for i in range(1,len(dataset)):
        print(dataset[i][0],"got total=",end=" ")
        total_votes=0
        for j in range(1,len(dataset)):
            total_votes+=int(dataset[i][j])
        print(total_votes)
##########################################################################
def total_votes_cast_by_each_state(dataset):
    for i in range(1,len(dataset)):
        print(dataset[0][i],"cast total=",end=" ")
        total_votes_of_each_state=0
        for j in range(1,len(dataset)):
            total_votes_of_each_state+=int(dataset[j][i])
        print(total_votes_of_each_state,"votes")
##########################################################################
def most_and_least_votes(dataset):
    count=list()
    for i in range(1,len(dataset)):
        total_votes=0
        for j in range(1,len(dataset)):
            total_votes+=int(dataset[i][j])
        count.append(total_votes)
    minpos= 1 + count.index(min(count))
    maxpos= 1 + count.index(max(count))

    print("Maximum vote got by: ",dataset[minpos][0])
    print("Maximum vote got by: ",dataset[maxpos][0])
##########################################################################
def sorting(a):
    for i in range(len(a[0])):
        for j in range((len(a[0])-i-1)):
            if int(a[1][j])>int(a[1][j+1]):
                temp1=a[1][j]
                temp0=a[0][j]

                a[1][j]=a[1][j+1]
                a[0][j]=a[0][j+1]

                a[1][j+1]=temp1
                a[0][j+1]=temp0
    return a
        
def sort_each_candidate_votes(dataset):
    
    for i in range(1,len(dataset)):
        count=list()
        count.append(dataset[0][1:])
        count.append(dataset[i][1:])
        
        count=sorting(count)
        
        print(dataset[i][0],"has got votes:")
        for j in range(len(count[0])):
            print(count[0][j],"=",count[1][j])
        print("\n")
#######################################################################

def main():
    dataset=csv()
    print("The Data set is:")
    for i in dataset:
        print(i)

    print("\nName of the States are:")
    for i in range(1,len(dataset)):
        print(dataset[0][i])

    print("\nName of the candidates are:")
    for i in range(1,len(dataset)):
        print(dataset[i][0])
    
    print("\n")
    min_max_votes(dataset)
    print("\n")
    total_votes(dataset)
    print("\n")
    total_votes_cast_by_each_state(dataset)
    print("\n")
    most_and_least_votes(dataset)
    print("\n")
    sort_each_candidate_votes(dataset)

main()

    
    



