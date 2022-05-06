import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.pyplot import figure


def graphStop(stopName, emb):
    file = 'Files/file1Dataframe.csv'
    fileDataFrame = pd.read_csv(file, low_memory=False, index_col=0)

    # print(fileDataFrame)
    # print(fileDataFrame.dtypes)

    dataforfretwell = fileDataFrame.loc[fileDataFrame['CorrectStop'] == stopName]
    dataforfretwell = dataforfretwell.reset_index()

    # print(dataforfretwell)

    fig = plt.figure()
    fig.set_figwidth(12)

    if emb == 0:
        dataforfretwell = dataforfretwell.query('OnOff =="on"')
    else:
        dataforfretwell = dataforfretwell.query('OnOff =="off"')

    dataforfretwell.plot(kind='line', x='Time', y='Count')
    if emb == 0:
        plt.title(stopName + ' Students Embarking the Bus')
    else:
        plt.title(stopName + ' Students Disembarking the Bus')
    plt.subplot()
    if emb == 0:
        plt.savefig("Graphs/" + stopName + "_Embark.png")
        plt.close()
        return "Graphs/" + stopName + "_Embark.png"
    else:
        plt.savefig("Graphs/" + stopName + "_Disembark.png")
        plt.close()
        return "Graphs/" + stopName + "_Disembark.png"

def graphBus(bus):

    file = 'Files/file1Dataframe.csv'

    fileDataFrame = pd.read_csv(file, low_memory=False, index_col=0)
    fileDataFrame["RunningTotal"] = np.nan
    # fileDataframe = fileDataFrame.reindex(columns = fileDataFrame.columns.tolist() + ["RunningTotal"])
    fileDataFrame['Time'] = fileDataFrame['Time'].astype(dtype='string')

    print(fileDataFrame)

    print(fileDataFrame.dtypes)

    datafor2401 = fileDataFrame.loc[fileDataFrame['Bus'] == bus]
    datafor2401 = datafor2401.reset_index()

    print(datafor2401)

    onBus = 0

    for i in range(0, len(datafor2401)):
        print(i, ":", datafor2401.OnOff[i])
        if datafor2401.OnOff[i] == "on":
            onBus = onBus + datafor2401.Count[i]
        else:
            onBus = onBus - datafor2401.Count[i]
        datafor2401.RunningTotal[i] = onBus

    print(datafor2401)

    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(5)

    datafor2401.plot(kind='line', x='Time', y='RunningTotal')
    plt.title('Students on the Bus')

    plt.show()

def create_graphs():
    file1 = 'Files/stops.csv'
    df = pd.read_csv(file1, low_memory=False, index_col=0)
    df['Stop'] = df['Stop'].astype(dtype='string')

    for i in range(0, len(df)):
        print(df.iloc[i].Stop)
        graphStop(df.iloc[i].Stop, 0)
        graphStop(df.iloc[i].Stop, 1)


def fillinGraph(dataframe, compareDataframe):
    x = 0
    cdfLength = compareDataframe.shape[0]
    while x != dataframe.shape[0]:
        if dataframe.loc[x].at["Stop"] != compareDataframe.loc[x % cdfLength].at["Stop"]:
            Date = dataframe.loc[x].at["Date"]
            Time = dataframe.loc[x].at["Time"] + 30
            Bus = dataframe.loc[x].at["Bus"]
            Count = 0
            OnOff = "on"
            Latitude = compareDataframe.loc[x % cdfLength].at["Latitude"]
            Longitude = compareDataframe.loc[x % cdfLength].at["Longitude"]
            Route = dataframe.loc[x].at["Route"]
            Stop = compareDataframe.loc[x % cdfLength].at["Stop"]
            dataline = pd.Series(data={"Date": Date, "Time": Time, "Bus": Bus, "Count": Count, "OnOff": OnOff,
                                       "Latitude": Latitude, "Longitude": Longitude, "Route": Route, "Stop": Stop,
                                       "CorrectStop": Stop}, name='x')
            dataframe.append(dataline, Ignore_Index=False)
        x = x + 1
    return dataframe
