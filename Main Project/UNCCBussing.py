from PIL import Image, ImageTk
import tkinter
import os
from tkintermapview import TkinterMapView

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("UNCC Bussing.py")

# create map widget
map_widget = TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(35.307044,	-80.734812)  # UNCC Campus
map_widget.set_zoom(16)

# load images in PhotoImage object
CRI_Board = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphs", "CRI Deck.png")).resize((500, 375)))
CRI_Disembark = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphs", "CRI Deck Off.png")).resize((500, 375)))
Lot6_Board = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphs", "Lot 6.png")).resize((500, 375)))
StUnE_Board = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphs", "Student Union E.png")).resize((500, 375)))


# create marker through .set_address() with image, which is visible at zoom levels 14 to infinity
#marker_1 = map_widget.set_address("35.3094,-80.7441", marker=True, image=CRI_Board, image_zoom_visibility=(14, float("inf")))

# make image visible/invisible when marker is clicked
def click_airport_marker_event(marker):
    print("marker clicked:", marker.text)
    if marker.image_hidden is True:
        marker.hide_image(False)
    else:
        marker.hide_image(True)

marker_1 = map_widget.set_marker(35.3090,-80.7436, text="CRI Deck Disembarking", image=CRI_Disembark,
                                 image_zoom_visibility=(0, float("inf")), command=click_airport_marker_event)
marker_1.hide_image(True)  # hide image

# create marker through .set_marker() with image, which is visible at all zoom levels
marker_2 = map_widget.set_marker(35.3094,-80.7441, text="CRI Deck Boarding", image=CRI_Board,
                                 image_zoom_visibility=(0, float("inf")), command=click_airport_marker_event)
marker_2.hide_image(True)  # hide image


marker_3 = map_widget.set_marker(35.308044,	-80.732712, text="Student Union East", image=StUnE_Board,
                                 image_zoom_visibility=(0, float("inf")), command=click_airport_marker_event)
marker_3.hide_image(True)  # hide image

marker_4 = map_widget.set_marker(35.3088,-80.7255, text="Lot 6", image=Lot6_Board,
                                 image_zoom_visibility=(0, float("inf")), command=click_airport_marker_event)
marker_4.hide_image(True)  # hide image

#marker_1 = map_widget.set_marker(35.308044,	-80.732712, text="Student Union East", text_color="green",
#                                 marker_color_circle="black", marker_color_outside="grey40", font=("Helvetica Bold", 16))

root_tk.mainloop()