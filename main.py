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
import OAuthCheck

start = timer()

class App:
    frames = {"f1": None, "f2": None}
    def __init__(self, root):
        
        App.frames['f1'] = customtkinter.CTkFrame(root)
        

        App.frames['f2'] = customtkinter.CTkFrame(root)



        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")


        root.geometry("1600x800")
        root.title("OSU Mentor Matcher!")
        root.resizable(False, False)
        # create a grid of 2 columns, 1 for sidebar, 1 for scrollable mentor list
        # possibly could change column weights to 1 and 3
        root.grid_columnconfigure((0, 1), weight=0)
        root.grid_rowconfigure((0, 1, 2, 3), weight=1)

        
        def runMatcher():
                # GUI.SidebarFrame.pack(fill="both", expand=True, padx=0, pady=0)
                # GUI.LoginFrame.pack_forget()
                # Matcher()
                App.frames['f2'].pack(fill="both", expand=True, padx=0, pady=0)
                App.frames['f1'].pack_forget()
                Matcher()
                

        def runLogin():
            GUI.LoginFrame.pack(fill="both", expand=True, padx=0, pady=0)
            GUI.SidebarFrame.pack_forget()
            Matcher()


        def Login():
            login_frame = GUI.LoginFrame(master=App.frames['f1'])
            App.frames['f1'].pack()
            login_frame.pack(pady=20, padx=60, fill="both", expand=True)
            login_label = customtkinter.CTkLabel(App.frames['f1'], text="Login System", font=("Roboto", 24))
            login_label.pack(pady=12, padx=10)

            client_id_entry = customtkinter.CTkEntry(App.frames['f1'], placeholder_text="Client ID", show="*")
            client_id_entry.pack(pady=12, padx=10)

            client_key_entry = customtkinter.CTkEntry(App.frames['f1'], placeholder_text="Client Secret", show="*")
            client_key_entry.pack(pady=12, padx=10)

            username_entry = customtkinter.CTkEntry(App.frames['f1'], placeholder_text="username")
            username_entry.pack(pady=12, padx=10)

            login_button = customtkinter.CTkButton(App.frames['f1'], text="Login", command=runMatcher)
            login_button.pack(pady=12, padx=12)
            login_button = customtkinter.CTkButton(App.frames['f1'], text="Get Osu OAuth", command=OAuthCheck.new_OAuth)
            login_button.pack(pady=12, padx=14)

        

        
        def Matcher():

            # # load images with light and dark mode image
            # image_file = "osuIconRevised.png"
            # image = tk.PhotoImage(file = image_file)

            sidebar_frame = GUI.SidebarFrame(master=App.frames['f2'])
            sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            # sidebar_frame.grid_propagate(False)
            sidebar_frame.grid_rowconfigure(4, weight=1) # stretches sidebar to the bottom of the window

            lblScrapeLimit = customtkinter.CTkLabel(App.frames['f2'],text = "Scraping Limit:")
            lblScrapeLimit.place(x=50,y=100)
            txtScrapingLimit = customtkinter.CTkEntry(App.frames['f2'])
            txtScrapingLimit.place(x=50,y=125)

            lblStartRank = customtkinter.CTkLabel(App.frames['f2'],text = "Starting Rank:")
            lblStartRank.place(x=50,y=175)
            txtStartRank = customtkinter.CTkEntry(App.frames['f2'])
            txtStartRank.place(x=50,y=200)

            lblEndRank = customtkinter.CTkLabel(App.frames['f2'],text = "Ending Rank:")
            lblEndRank.place(x=50,y=250)
            txtEndRank = customtkinter.CTkEntry(App.frames['f2'])
            txtEndRank.place(x=50,y=275)
            def btnEnter():
                scraping_limit = int(txtScrapingLimit.get())
                starting_rank = int(txtStartRank.get())
                ending_rank = int(txtEndRank.get())
                if scraping_limit < 1 :
                    messagebox.showerror("Error", "Invalid Scraping Limit!")
                elif starting_rank < 1:
                    messagebox.showerror("Error", "Invalid Starting Rank!")
                elif scraping_limit < 1 and starting_rank < 1 : 
                    messagebox.showerror("Error", "Invalid Scraping Limit and Starting Rank!")

                
            btnEnter = customtkinter.CTkButton(App.frames['f2'], text = "Enter", command=btnEnter)
            btnEnter.place(x=50,y=350)

            def label_button_frame_event(item):
                print(f"label button frame clicked: {item}")

            scrollable_mentor_frame = GUI.ScrollableMentorFrame(master=App.frames['f2'], width=1250, command=label_button_frame_event, corner_radius=0)
            scrollable_mentor_frame.grid(row=0, rowspan=4, column=1, padx=40, pady=0, sticky="nsew")

            for i in range(20):  # add items with images
                scrollable_mentor_frame.add_item(f"Username {i}", image=None)

        Login()
       


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()
    
