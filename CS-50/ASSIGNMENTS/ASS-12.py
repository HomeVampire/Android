#IMPORT AN CSV FILE
def csv():
    import csv
    dataset=list()
    with open('C:\WORK\PROGRAM\PYTHON\CS-50\DATASETS\Time_series_19_covid_Confirmed.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            dataset.append(line)
    return dataset
#######################################################################
##CREATE A DICTIONARY
def create_dictionary(dataset):
    countries=dict()

    for i in range(1,len(dataset)):
        countries[dataset[i][1]]={} ## Khub important line 1
    for i in range(1,len(dataset)):
        countries[dataset[i][1]][dataset[i][0]]={} ## Khub important line 2

    for i in range(1,len(dataset)):
        dataset_for_timeseries=list()
        for j in range(4,len(dataset[0])):
            dataset_for_timeseries.append((dataset[0][j], dataset[i][j]))
            ##dataset_for_timeseries.append(dataset[i][j])
        coordinates=list()
        coordinates.append((dataset[i][2], dataset[i][3]))
        ##coordinates.append(dataset[i][3])
        countries[dataset[i][1]][dataset[i][0]]['coordinaates']=coordinates
        countries[dataset[i][1]][dataset[i][0]]['timeseries']=dataset_for_timeseries


    print(countries[dataset[1][1]][dataset[1][0]]['timeseries'][-1][1])

#######################################################################
def main():
    dataset=csv()

    for i in range(len(dataset)):
        if len(dataset[i][0])==0:
            dataset[i][0]='n/a'
    
    create_dictionary(dataset) 

main()
