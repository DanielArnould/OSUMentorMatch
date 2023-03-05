from ossapi import *
import configparser
import OSUUtils, GUI
from timeit import default_timer as timer
import customtkinter 
import tkinter as tk

import os
# from PIL import Image
from PIL import Image
import urllib.request



start = timer()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1600x800")
root.title("OSU Mentor Matcher!")
root.resizable(False, False)
# create a grid of 2 columns, 1 for sidebar, 1 for scrollable mentor list
# possibly could change column weights to 1 and 3
root.grid_columnconfigure((0, 1), weight=0)
root.grid_rowconfigure((0, 1, 2, 3), weight=1)




# login_frame = GUI.LoginFrame(master=root)
# login_frame.pack(pady=20, padx=60, fill="both", expand=True)



# # load images with light and dark mode image
# image_file = "osuIconRevised.png"
# image = tk.PhotoImage(file = image_file)

sidebar_frame = GUI.SidebarFrame(master=root)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
# sidebar_frame.grid_propagate(False)
sidebar_frame.grid_rowconfigure(4, weight=1) # stretches sidebar to the bottom of the window

def label_button_frame_event(item):
    print(f"label button frame clicked: {item}")

scrollable_mentor_frame = GUI.ScrollableMentorFrame(master=root, width=1250, command=label_button_frame_event, corner_radius=0)
scrollable_mentor_frame.grid(row=0, rowspan=4, column=1, padx=40, pady=0, sticky="nsew")

for i in range(20):  # add items with images
    scrollable_mentor_frame.add_item(f"Username {i}", image=None)


root.mainloop()
