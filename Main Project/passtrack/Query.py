import csv
import pandas as pd

file1 = 'Files/file1Dataframe.csv'

file1Dataframe = pd.read_csv(file1, low_memory=False)


class Query:
    def __init__(self, enterDataFrame, columnElement, columnTitle):
        self.enterDataFrame = enterDataFrame
        self.columnElement = columnElement
        self.columnTitle = columnTitle

    def queryItem(self):
        if self.columnTitle not in self.enterDataFrame.columns:
            print("Error: The Column does not exist")
            return 0
        queryString = str(self.columnTitle) + ' == ' + str(self.columnElement)
        self.enterDataFrame.query(queryString, inplace=True)
        if self.enterDataFrame.empty:
            print('No Results for Query')
            return 0
        return self.enterDataFrame

