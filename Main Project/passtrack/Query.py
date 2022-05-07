import csv
import pandas as pd

file1 = 'Files/file1Dataframe.csv'

file1Dataframe = pd.read_csv(file1, low_memory=False)


def queryItem(enterDataFrame, query):
    #if columnTitle not in enterDataFrame.columns:
    #    print("Error: The Column does not exist")
    #    return 0
    queryString = str(columnTitle) + ' == ' + str(columnElement)
    enterDataFrame.query(queryString, inplace=True)
    if enterDataFrame.empty:
        print('No Results for Query')
        return 0
    return enterDataFrame

