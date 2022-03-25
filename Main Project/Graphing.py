import csv
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from matplotlib.pyplot import figure

def graphStop():
    file = 'Files/file1Dataframe.csv'
    fileDataFrame = pd.read_csv(file, low_memory=False, index_col=0)

    print(fileDataFrame)
    print(fileDataFrame.dtypes)

    stopName = "Student Union E"

    dataforfretwell = fileDataFrame.loc[fileDataFrame['CorrectStop'] == stopName]
    dataforfretwell = dataforfretwell.reset_index()

    print(dataforfretwell)

    f = plot.figure()
    f.set_figwidth(6)

    dataforfretwell = dataforfretwell.query('OnOff =="on"')

    dataforfretwell.plot(kind = 'line', x='Time',y ='Count')
    plot.title(stopName + ' Students Boarding the Bus')
    plot.show()
    #f.savefig("Graphs/" + stopName)
def graphBus():


    file = 'Files/file1Dataframe.csv'

    fileDataFrame = pd.read_csv(file, low_memory=False, index_col=0)
    fileDataFrame["RunningTotal"] = np.nan
    # fileDataframe = fileDataFrame.reindex(columns = fileDataFrame.columns.tolist() + ["RunningTotal"])
    fileDataFrame['Time'] = fileDataFrame['Time'].astype(dtype='string')

    print(fileDataFrame)

    print(fileDataFrame.dtypes)

    datafor2401 = fileDataFrame.loc[fileDataFrame['Bus'] == 2401]
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

    f = plot.figure()
    f.set_figwidth(10)
    f.set_figheight(5)

    datafor2401.plot(kind='line', x='Time', y='RunningTotal')
    plot.title('Students on the Bus')

    plot.show()


graphBus()