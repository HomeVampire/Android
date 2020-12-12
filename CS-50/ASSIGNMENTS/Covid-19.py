import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.mohfw.gov.in/'

# make a GET request to fetch the raw HTML content
html_content = requests.get(url).content

# parse the html content
soup = BeautifulSoup(html_content, "lxml")

covid_table = soup.find("table", attrs={"class": "table table-striped"})

heading=[]
for row in covid_table.thead.find_all("th"):
    heading.append(row.text.replace('\n', ' ').strip())

covid_content=[]
for tr in covid_table.tbody.find_all("tr"):
    row=[]
    for td in tr.find_all("td"):
        row.append(td.text.replace('\n', ' ').strip())

    covid_content.append(row)

df=pd.DataFrame(data =covid_content, columns =heading)
df=df[0:35]

i=int(input("Press 1 to view COVID-19 details\nPress any key to Store only details as CSV..."))
print()
if i==1:
    print(df)
    choice = input("Do you want to see the details as Bar Chart......(y/n)")
    if choice == 'y':
        sns.set_style("ticks")
        plt.figure(figsize=(30, 20))
        plt.barh(df['Name of State / UT'], df['Active Cases*'], align='center', color='blue')
        plt.xlabel('No. of Active Cases*', fontsize=15)
        plt.ylabel('Name of State / UT', fontsize=15)
        plt.xticks(fontsize=10, rotation='vertical')
        plt.yticks(fontsize=10)
        plt.title('COVID-19 ACTIVE CASES IN INDIA', fontsize=15)

        for index, value in enumerate(df['Active Cases*']):
            plt.text(value, index, str(value), fontsize=10)
        plt.show()

else:
    directory_path = os.path.join(os.getcwd(), 'COVID-19/')
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    df.to_csv(directory_path+'Covid-19.csv', index=False)





