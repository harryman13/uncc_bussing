import csv
import pandas as pd
import matplotlib.pyplot as plot

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