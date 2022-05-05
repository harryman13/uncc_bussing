from tkintermapview import TkinterMapView
import customtkinter
from PIL import Image, ImageTk
import pandas as pd
import Query
import Graphing

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
                                                command=self.map_widget.toggle_mode,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_4.grid(pady=10, padx=20, row=4, column=0)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Gold Route",
                                                command=self.map_widget.toggle_mode,
                                                width=120, height=30,
                                                border_width=0,
                                                corner_radius=8)
        self.button_5.grid(pady=10, padx=20, row=5, column=0)

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Green Route",
                                                command=self.map_widget.toggle_mode,
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

            CRI_Embark = ImageTk.PhotoImage(Image.open("Graphs/CRI Deck_Disembark.png").resize((500, 375)))
            CRI_Disembark = ImageTk.PhotoImage(Image.open("Graphs/CRI Deck_Embark.png").resize((500, 375)))

            for i in range(0, len(df)):
                print("Stop: " + df.iloc[i].Stop)
                # self.img_list.append(
                #    [ImageTk.PhotoImage(Image.open(graphStop(df.iloc[i].Stop, 0)).resize((500, 375))),
                #    ImageTk.PhotoImage(Image.open(graphStop(df.iloc[i].Stop, 1)).resize((500, 375)))])
                # print(self.img_list[i])

                self.img_list.append(
                    [ImageTk.PhotoImage(Image.open("Graphs/" + df.iloc[i].Stop + "_Embark.png").resize((500, 375))),
                     ImageTk.PhotoImage(Image.open("Graphs/" + df.iloc[i].Stop + "_Disembark.png").resize((500, 375)))])

                mark = self.map_widget.set_marker(df.iloc[i].Latitude, df.iloc[i].Longitude, text=df.iloc[i].Stop,
                                                  image=(self.img_list[i]),
                                                  image_zoom_visibility=(14, 20), command=click_marker_event)

                # mark = self.map_widget.set_marker(df.iloc[i].Latitude, df.iloc[i].Longitude, text=df.iloc[i].Stop, image=(CRI_Embark,CRI_Disembark),
                #                                  image_zoom_visibility=(0, float("inf")), command=click_marker_event)
                self.marker_list.append(mark)
                self.marker_list[i].hide_image(True)  # hide image
                # mark.hide_image(True)

        stop_setup(self, 'Files/stops.csv')

        # path_1 = self.map_widget.set_path(
        #     [(35.3088015, -80.725095), (35.3085796, -80.7249403), (35.3083695, -80.7247123), (35.3081550, -80.7243637),
        #      (35.3079398, -80.7245085), (35.3076684, -80.7246238), (35.3075448, -80.7246252), (35.3075448, -80.7246252),
        #      (35.3072492, -80.7246995),
        #      (35.3072, -80.7252), (35.3069544, -80.7259399), (35.3065775, -80.7264477),
        #      (35.3063, -80.7268), (35.3057436, -80.7276113), (35.3056129, -80.7278711), (35.3055801, -80.7280159),
        #      (35.3056042, -80.7280803), (35.3058887, -80.7281125), (35.3061645, -80.7281957), (35.3067117, -80.7292148),
        #      (35.3067748, -80.7293539), (35.3069652, -80.7294317), (35.3073942, -80.7293646),
        #      (35.3075909, -80.7293211), (35.3080882, -80.7293378),
        #      (35.30813, -80.73268), (35.3081026, -80.7336427), (35.3080194, -80.7344297), (35.3079417, -80.7364360),
        #      (35.3079885, -80.7374952), (35.3078579, -80.7379666), (35.3077069, -80.7381784), (35.3075055, -80.7384493),
        #      (35.3072910, -80.7390207), (35.3073129, -80.7391709), (35.3073391, -80.7395211),
        #      (35.307468, -80.739724), (35.3075886, -80.7400530), (35.3079607, -80.7404392), (35.3082802, -80.7405304),
        #      (35.3086348, -80.7405412), (35.3089500, -80.7406806), (35.3091164, -80.7409167),
        #      (35.3093526, -80.7412905), (35.3094356, -80.7414209), (35.3097180, -80.7416811), (35.3100069, -80.7418018),
        #      (35.3103833, -80.7418233), (35.3105355, -80.7417630), (35.3108091, -80.7415833), (35.3112179, -80.7411996),
        #      (35.3114954, -80.7409257), (35.3119703, -80.7402095), (35.3122822, -80.7403007), (35.3126235, -80.7407379),
        #      (35.3129037, -80.7411698),
        #      (35.3123682, -80.7416682),
        #      (35.31106, -80.74313), (35.3094268, -80.7448061), (35.3092335, -80.7444384),
        #      (35.3094, -80.7441), (35.3095004, -80.7440576), (35.3097478, -80.7443875),
        #      (35.31164, -80.74249), (35.3128946, -80.7411730), (35.3122992, -80.7403093), (35.3119972, -80.7402074),
        #      (35.3116689, -80.7407760),
        #      (35.31102, -80.74141), (35.3106774, -80.7417053), (35.3103748, -80.7418433),
        #      (35.309912, -80.741863), (35.3095377, -80.7415949), (35.3093188, -80.7413051), (35.3089308, -80.7406431),
        #      (35.3084230, -80.7405197), (35.3079721, -80.7404178), (35.3076394, -80.7401550),
        #      (35.3074213, -80.7398642), (35.3073242, -80.7394286), (35.3073001, -80.7391577), (35.3073439, -80.7388225),
        #      (35.3075234, -80.7383987), (35.3077253, -80.7381707), (35.3079442, -80.7377469), (35.3079595, -80.7372855),
        #      (35.3079290, -80.7364997), (35.3079378, -80.7352524),
        #      (35.3079418, -80.7348023), (35.3080797, -80.7340947), (35.3080819, -80.7331050),
        #      (35.30809, -80.73272), (35.3080733, -80.7306016),
        #      (35.3080697, -80.7305971), (35.3080983, -80.7293290),
        #      (35.3090450, -80.7292962),
        #      (35.3107, -80.7293), (35.3109019, -80.7292814), (35.3108691, -80.7290482), (35.3109180, -80.7284169),
        #      (35.3108940, -80.7280495), (35.3106773, -80.7274627), (35.3104584, -80.7269531),
        #      (35.310244, -80.726491), (35.3098041, -80.7254578), (35.3096071, -80.7252298), (35.3093086, -80.7251677),
        #      (35.3088015, -80.725095)
        #      ])



    def slider_event(self, value):
        self.map_widget.set_zoom(value)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

