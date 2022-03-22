import csv
import pandas as pd

file1 = '2018-2019 Stop Data PART 1.csv'
file2 = '2018-2019 Stop Data PART 2.csv'

file1Dataframe = pd.read_csv(file1, low_memory=False)
file2Dataframe = pd.read_csv(file2, low_memory=False)

print(file1Dataframe.dtypes)

ddfile1 = file1Dataframe.drop_duplicates('Stop')

print(ddfile1)

print(file1Dataframe)
file1Dataframe.loc[:, "ConstantLatitude"] = file1Dataframe.groupby('Stop').transform(
    lambda x: ddfile1.query('Stop == @x').loc[0, "Latitude"])

file1Dataframe.loc[:, "ConstantLongitude"] = file1Dataframe.groupby('Stop').transform(
    lambda x: ddfile1.query('Stop == @x').loc[0, "Longitude"])

print(file1Dataframe)
