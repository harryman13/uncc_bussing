#main file to run everything
from tkinter import *

#import numpy as np
#import matplotlib.pyplot as plt

root = Tk()
root.title('Generic Title')
root.geometry("1400x800")

#def graph():
#    house_prices = np.random.normal(200000, 25000, 5000)
#    plt.hist(house_prices, 50)
#    plt.show()

#my_button = Button(root, text="Graph It!", command=graph)
#mybutton.pack()

myLabel = Label(root, text = "Hello World!")

myLabel.pack()

root.mainloop()