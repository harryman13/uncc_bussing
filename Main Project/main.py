from tkintermapview.map_widget import TkinterMapView
import customtkinter
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
from passtrack import Graphing as gr
from passtrack import Busses as b
from passtrack import Query


class App(customtkinter.CTk):

    APP_NAME = "UNCC Bussing"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        self.img_list = []
        self.pause = False


        def click_marker_event(marker):
            print("marker clicked:", marker.text)
            if marker.image_hidden is True:
                marker.hide_image(False)
            else:
                marker.hide_image(True)

    # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=150)
        self.frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  corner_radius=10)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=20, padx=20, sticky="nsew")

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, width=450, height=250, corner_radius=9)
        self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=20, pady=20)
        self.map_widget.set_position(35.307044, -80.734812)  # UNCC Campus
        self.map_widget.set_zoom(16)

        self.SilverPathFile = pd.read_csv('Files/SilverDetailed.csv', index_col=0)
        self.SilverPathFile = self.SilverPathFile.drop(columns="isStop")
        self.SilverPathFile = self.SilverPathFile.drop(columns="Stop")
        self.SilverPathFile = self.SilverPathFile.values
        self.SilverPath = None

        #self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                    placeholder_text="type address",
        #                                    width=140,
        #                                    height=30,
        #                                    corner_radius=8)
        #self.entry.grid(row=1, column=0, sticky="we", padx=20, pady=20)
        #self.entry.entry.bind("<Return>", self.search_event)

        #self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                        height=30,
        #                                        text="Search",
        #                                        command=self.search_event,
        #                                        border_width=0,
        #                                        corner_radius=8)
        #self.button_5.grid(row=1, column=1, sticky="w", padx=10, pady=20)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                width=1000,
                                                height=16,
                                                from_=0, to=19,
                                                border_width=5,
                                                command=self.slider_event)
        self.slider_1.grid(row=1, column=1, sticky="e", padx=20, pady=20)
        self.slider_1.set(self.map_widget.zoom)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)

        #self.button_1 = customtkinter.CTkButton(master=self.frame_left,
        #                                        text="Set Marker",
        #                                        command=self.set_marker_event,
        #                                        width=120, height=30,
        #                                        border_width=0,
        #                                        corner_radius=8)
        #self.button_1.grid(pady=10, padx=20, row=3, column=0)

        #self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                        text="Clear Markers",
        #                                        command=self.clear_marker_event,
        #                                        width=120, height=30,
        #                                        border_width=0,
        #                                        corner_radius=8)
        #self.button_2.grid(pady=10, padx=20, row=4, column=0)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                               text="Embark/Disembark",
                                                command=self.map_widget.toggle_mode,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_3.grid(pady=10, padx=20, row=3, column=0)

        self.button_4= customtkinter.CTkButton(master=self.frame_left,
                                                text="Silver Route",
                                                command=self.silverToggle,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_4.grid(pady=10, padx=20, row=4, column=0)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Gold Route",
                                                command=self.silverToggle,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_5.grid(pady=10, padx=20, row=5, column=0)

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Green Route",
                                                command=self.map_widget.insert_stop,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_6.grid(pady=10, padx=20, row=6, column=0)

        self.button_7 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Settings",
                                                command=self.map_widget.toggle_mode,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_7.grid(pady=10, padx=20, row=7, column=0)

        self.button_8 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Dashboard",
                                                command=self.map_widget.toggle_mode,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_8.grid(pady=10, padx=20, row=8, column=0)

        def stop_setup(self, file):
            file = 'Files/stops.csv'
            df = pd.read_csv(file, low_memory=False, index_col=0)
            df['Stop'] = df['Stop'].astype(dtype='string')

            # print(df.dtypes)

            #CRI_Embark = ImageTk.PhotoImage(Image.open("Graphs/CRI Deck_Disembark.png").resize((500, 375)))
            #CRI_Disembark = ImageTk.PhotoImage(Image.open("Graphs/CRI Deck_Embark.png").resize((500, 375)))

            #gr.create_graphs()

            for i in range(0, len(df)):
                print("Stop: " + df.iloc[i].Stop)
                #self.img_list.append(
                #   [ImageTk.PhotoImage(Image.open(graphStop(df.iloc[i].Stop, 0)).resize((500, 375))),
                #   ImageTk.PhotoImage(Image.open(graphStop(df.iloc[i].Stop, 1)).resize((500, 375)))])
                # print(self.img_list[i])
                image1 = ("Graphs/" + df.iloc[i].Stop + "_Embark.png")
                image2 = ("Graphs/" + df.iloc[i].Stop + "_Disembark.png")
                print(image1)
                print(image2)
                self.img_list.append(
                    [ImageTk.PhotoImage(Image.open(image1).resize((500, 375))),
                     ImageTk.PhotoImage(Image.open(image2).resize((500, 375)))])

                mark = self.map_widget.set_marker(df.iloc[i].Latitude, df.iloc[i].Longitude, text=df.iloc[i].Stop,
                                                  image=(self.img_list[i]),
                                                  image_zoom_visibility=(14, 20), command=click_marker_event)

                # mark = self.map_widget.set_marker(df.iloc[i].Latitude, df.iloc[i].Longitude, text=df.iloc[i].Stop, image=(CRI_Embark,CRI_Disembark),
                #                                  image_zoom_visibility=(0, float("inf")), command=click_marker_event)
                self.marker_list.append(mark)
                self.marker_list[i].hide_image(True)  # hide image
                # mark.hide_image(True)

        stop_setup(self, 'Files/stops.csv')

        file1 = pd.read_csv('Files/file1Dataframe.csv', index_col=0)
        file1 = gr.fix(file1)
        file1.to_csv('Files/file1New.csv')
        self.uniqueBuses = file1.Bus.unique()
        self.bus = []
        for i in self.uniqueBuses:
            print(i)
            temp = file1.query("Bus == "+str(i))
            temp = temp.reset_index()
            temp = temp.drop(columns="index")
            temp = gr.dt(temp)
            self.bus.append(b.Bus(2407, 0, temp, self.map_widget))

        for i in self.bus:
            i.flatten()
            i.detailedRoute = gr.fillinGraph(i.route, i.route.iloc[0].at["Route"])
            i.detailedRoute.to_csv("Files/BusRoutes/" + str(i.BusNumber) + ".csv")
        temp = file1.query("Bus ==  2407")
        temp = temp.reset_index()
        temp = temp.drop(columns="index")
        temp = gr.dt(temp)
        self.bus = b.Bus(2407, 0, temp, self.map_widget)
        self.bus.flatten()
        self.bus.detailedRoute = gr.fillinGraph(self.bus.route, "Silver")

        #bus_x, bus_y = self.bus.getPos(0)
        #self.bus.set_position(bus_x, bus_y)

        #self.time = self.bus.route.DateTime

    def slider_event(self, value):
        self.map_widget.set_zoom(value)

    def silverToggle(self):
        print("silverToggle")
    #    if self.SilverPath is None:
    #        self.SilverPath = self.map_widget.set_path(self.SilverPathFile)
    #    else:
    #        self.SilverPath.delete()

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def upd(self):
        if not self.pause:
            self.time = self.time + pd.Timedelta(seconds = 10)
            bus


if __name__ == "__main__":
    app = App()

    #set update time

    #app.after(app.update_time, app.upd)
    app.start()
    #while True:
    #    app.update_idletasks()
    #    app.update()


