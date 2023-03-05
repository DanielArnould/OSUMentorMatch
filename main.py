from ossapi import *
import configparser
import OSUUtils, GUI
from timeit import default_timer as timer
import customtkinter 
import tkinter as tk

import os
# from PIL import Image



start = timer()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1600x800")
root.title("OSU Mentor Matcher!")
# create a grid of 2 columns, 1 for sidebar, 1 for scrollable mentor list
# possibly could change column weights to 1 and 3
root.grid_columnconfigure((0, 1), weight=0)
root.grid_rowconfigure((0, 1, 2, 3), weight=1)




login_frame = GUI.LoginFrame(master=root)
login_frame.pack(pady=20, padx=60, fill="both", expand=True)



# load images with light and dark mode image
image_file = "osuIconRevised.png"
image = tk.PhotoImage(file = image_file)

label = tk.Label(root, image=image)
label.pack()


root.mainloop()
