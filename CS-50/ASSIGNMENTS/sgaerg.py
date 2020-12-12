i = int(input("Press 1 to view GDP and store as CSV\nPress any key to Store only details as CSV..."))
print()

for topic, table in data.items():
    directory_path = os.path.join(os.getcwd(), 'OUTPUT/')
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

    # Create csv file for each table
    with open(directory_path + topic + '.csv', 'w', newline='') as out_file:
        # Each 3 table has headers as following
        headers = ["Rank", "Country/Territory", "GDP(US$million)"]  # == t_headers
        writer = csv.writer(out_file)
        writer.writerow(headers)
        for row in table:
            if (row):
                writer.writerow(row)
    #######################################################################   Use panda to show in a table
    if i == 1:
        print(topic)
        df = pd.read_csv(directory_path + topic + '.csv', encoding="ISO-8859-1")
        new_df = df.replace([''], np.NaN)
        print(new_df)
        #######################################################################
        choice = input("Do you want to see the details as Bar Chart......(y/n)")
        if choice == 'y':
            n = int(input("For how many countries you want to see the data Sheet..."))
            new_df = new_df[1:n + 1]

            sns.set_style("ticks")
            plt.figure(figsize=(30, 20))
            plt.barh(new_df['Country/Territory'], new_df['GDP(US$million)'], align='center', color='blue')
            plt.xlabel('GDP Amount', fontsize=15)
            plt.ylabel('Country Name', fontsize=15)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            plt.title(topic, fontsize=15)

            for index, value in enumerate(new_df["GDP(US$million)"]):
                plt.text(value, index, str(value), fontsize=10)
            plt.show()