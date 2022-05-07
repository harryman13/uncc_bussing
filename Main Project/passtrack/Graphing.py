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

def dt(df):

    df["DateTime"] = pd.to_datetime((df['Date'] + ' ' + df['Time']))# , format= '%m/%d/%y %H:%M:%S')
    df = df.drop(columns="Time")
    df = df.drop(columns="Date")
    print(df)
    return df

def nextStop(dataframe, index):
    for i in range(index,len(dataframe)):
        if dataframe.iloc[i].at("isStop") == "Yes":
            return i

def fillinGraph(dataframe, route):
    x = 0
    if route == "Silver":
        compareDataframe = pd.read_csv("Files/SilverRoute.csv",index_col=0)
    elif route == "Gold":
        compareDataframe = pd.read_csv("Files/GoldRoute.csv",index_col=0)
    elif route == "Green":
        compareDataframe = pd.read_csv("Files/GreenRoute.csv",index_col=0)

    cdfLength = len(compareDataframe)
    while x < len(dataframe):
        print("x:", x)
        print(dataframe.iloc[x].at["CorrectStop"], " : ", compareDataframe.iloc[x % cdfLength].at["Stop"])
        if dataframe.iloc[x].at["CorrectStop"] != compareDataframe.iloc[x % cdfLength].at["Stop"]:
            #print("in loop")
            DateTime = dataframe.iloc[x-1].at["DateTime"] + pd.Timedelta(seconds = 15)
            Bus = dataframe.iloc[x].at["Bus"]
            Count = 0
            OnOff = "on"
            Latitude = compareDataframe.iloc[x % cdfLength].at["Latitude"]
            Longitude = compareDataframe.iloc[x % cdfLength].at["Longitude"]
            Route = dataframe.iloc[x].at["Route"]
            Stop = compareDataframe.iloc[x % cdfLength].at["Stop"]
            dataline = pd.Series(data={"DateTime": DateTime, "Bus": Bus, "Count": Count, "OnOff": OnOff,
                                       "Latitude": Latitude, "Longitude": Longitude, "Route": Route, "Stop": Stop,
                                       "CorrectStop": Stop}, name='x')
            dataline = dataline.transpose()
            #print(dataline)
            #dataframe = pd.concat([dataframe, dataline], ignore_index= True)
            dataframe.loc[x-.5] = dataline
            dataframe = dataframe.sort_index().reset_index(drop=True)
        x = x + 1
    return dataframe

def fix(DataFrame):
    for i in range(0,len(DataFrame)):
        if DataFrame.CorrectStop[i] == "Levine Hall E":
            if DataFrame.Route[i] == "Gold":
                DataFrame.CorrectStop[i] = "Levine Hall W"

        elif DataFrame.CorrectStop[i] == "Levine Hall W" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Levine Hall E"

        elif DataFrame.CorrectStop[i] == "Student Health (Green) W" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Student Health E"

        elif DataFrame.CorrectStop[i] == "Student Health E" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Student Health (Green) W"

        elif DataFrame.CorrectStop[i] == "Student Union E" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Student Union W"

        elif DataFrame.CorrectStop[i] == "Student Union W" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Student Union E"

        elif DataFrame.CorrectStop[i] == "Wallis Hall W" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Wallis Hall E"

        elif DataFrame.CorrectStop[i] == "Wallis Hall E" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Wallis Hall W"

        elif DataFrame.CorrectStop[i] == "Cone Deck W" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Cone Deck East"

        elif DataFrame.CorrectStop[i] == "Cone Deck East" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Cone Deck W"

        elif DataFrame.CorrectStop[i] == "Hickory Hall North" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Hickory Hall South"

        elif DataFrame.CorrectStop[i] == "Hickory Hall South" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Hickory Hall North"

        elif DataFrame.CorrectStop[i] == "Hickory Hall South" and DataFrame.Route[i] == "Silver":
            DataFrame.CorrectStop[i] = "Hickory Hall North"

        elif DataFrame.CorrectStop[i] == "Aux Services East" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Fretwell N"

        elif DataFrame.CorrectStop[i] == "Belk Hall S" and DataFrame.Route[i] == "Gold":
            DataFrame.CorrectStop[i] = "Union Deck"

        elif DataFrame.CorrectStop[i] == "Union Deck" and DataFrame.Route[i] == "Green":
            DataFrame.CorrectStop[i] = "Belk Hall S"

        elif DataFrame.CorrectStop[i] == "Fretwell S" and DataFrame.Route[i] == "Silver":
            DataFrame.CorrectStop[i] = "Fretwell N"

        elif DataFrame.CorrectStop[i] == "Alumni Way E" and DataFrame.Route[i] == "Silver":
            DataFrame.CorrectStop[i] = DataFrame.Stop[i]

        elif DataFrame.CorrectStop[i] == "Belk Hall S" and DataFrame.Route[i] == "Silver":
            DataFrame.CorrectStop[i] = DataFrame.Stop[i]

        elif DataFrame.CorrectStop[i] == "Cato Hall N" and DataFrame.Route[i] == "Silver":
            DataFrame.CorrectStop[i] = DataFrame.Stop[i]
    return DataFrame