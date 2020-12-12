# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'nyc_weather.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("nyc_weather.csv", encoding="ISO-8859-1")
# Preview the first 5 lines of the loaded data 
print(data)