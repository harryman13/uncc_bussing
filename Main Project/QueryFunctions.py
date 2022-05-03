import csv
import pandas as pd

file1 = 'file1Dataframe.csv'

file1Dataframe = pd.read_csv(file1, low_memory=False)


class Query:
    def __init__(self):
        pass

    @staticmethod
    def queryItem(enterDataFrame, columnElement, columnTitle):
        if columnTitle not in enterDataFrame.columns:
            print("Error: The Column does not exist")
            return 0
        queryString = str(columnTitle) + ' == ' + str(columnElement)
        enterDataFrame.query(queryString, inplace=True)
        if enterDataFrame.empty:
            print('No Results for Query')
            return 0
        return enterDataFrame
