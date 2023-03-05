from ossapi import *
import configparser
import OSUUtils, GUI
import customtkinter 

import os
from PIL import Image
import urllib.request


# client_id : int
# client_secret: str
# username : str
# user: User

# config = configparser.RawConfigParser()
# config.read('config.cfg')
# keys_dict = dict(config.items('CONFIG'))

# client_id = keys_dict['client_id']
# client_secret = keys_dict['client_secret']
# username = keys_dict['user']


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x800")
root.title("OSU Mentor Matcher!")
root.resizable(False, False)
root.deiconify()
# create a grid of 2 columns, 1 for sidebar, 1 for scrollable mentor list
# possibly could change column weights to 1 and 3
root.grid_columnconfigure((0, 1), weight=0)
root.grid_rowconfigure((0, 1, 2, 3), weight=1)

# login_frame = GUI.LoginFrame(master=root)
# login_frame.pack(pady=20, padx=60, fill="both", expand=True)


sidebar_frame = GUI.SidebarFrame(master=root)
sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
# sidebar_frame.grid_rowconfigure(4, weight=1) # stretches sidebar to the bottom of the window

root.mainloop()
