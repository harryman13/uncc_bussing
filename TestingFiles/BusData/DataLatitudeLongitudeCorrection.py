import csv
import pandas as pd

file1 = '2018-2019 Stop Data PART 1.csv'
file2 = '2018-2019 Stop Data PART 2.csv'

file1Dataframe = pd.read_csv(file1, low_memory=False)
file2Dataframe = pd.read_csv(file2, low_memory=False)

print(file1Dataframe.dtypes)

ddfile1 = file1Dataframe.drop_duplicates('Stop')

file1Dataframe['ConstantLatitude'] = ''
file1Dataframe['ConstantLongitude'] = ''

print(file1Dataframe)


print(ddfile1)