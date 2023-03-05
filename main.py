from ossapi import *
import configparser
import OSUUtils, GUI
from timeit import default_timer as timer
import customtkinter 
import tkinter as tk
from tkinter import messagebox
import os
# from PIL import Image
from PIL import Image
import urllib.request
import OAuthCheck

start = timer()


client_id : int
client_secret: str
username : str
user: User


config = configparser.RawConfigParser()
config.read('config.cfg')
keys_dict = dict(config.items('CONFIG'))

client_id = keys_dict['client_id']
client_secret = keys_dict['client_secret']
username = keys_dict['user']


api = Ossapi(client_id, client_secret)
api.scopes = [Scope.PUBLIC, Scope.IDENTIFY]

try:
    user = api.user(user=username, mode=GameMode.OSU, key=UserLookupKey.USERNAME)
except ValueError:
    print("USER DOES NOT EXIST, TERMINATING")
    quit()

utils = OSUUtils.Utils(api)

def authy():
    OAuthCheck.client_id = App.Login.client_id_entry.get() 
    OAuthCheck.client_secret = App.Login.client_key_entry.get()
    OAuthCheck.user_id = App.Login.username_entry.get()
    OAuthCheck.get_OAuth()
    config = OAuthCheck.user_info


class App:
    frames = {"f1": None, "f2": None}
    def __init__(self, root):
        
        App.frames['f1'] = customtkinter.CTkFrame(root)
        

        App.frames['f2'] = customtkinter.CTkFrame(root)



        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")


        root.geometry("800x800")
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
                authy()
                App.frames['f2'].pack()
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

            logo_image = customtkinter.CTkImage(Image.open("osuIconRevised.png"), size=(26, 26))
            
        
        

        
        def Matcher():

            # # load images with light and dark mode image
            # image_file = "osuIconRevised.png"
            # image = tk.PhotoImage(file = image_file)
            App.frames['f2'].pack()
            matcher_frame = GUI.ScrollableMentorFrame(master=App.frames['f2'])
            sidebar_frame = GUI.SidebarFrame(master=App.frames['f2'])

            

            sidebar_label = customtkinter.CTkLabel(App.frames['f2'], text="Sidebar!", font=("Roboto", 24))
            sidebar_label.grid(row=0, column=0, padx=90, pady=(20, 20))

            entry_top_played_beatmaps_scraping_limit = customtkinter.CTkEntry(App.frames['f2'], width=250, placeholder_text="Top Played Beatmaps Scraping Limit")
            entry_top_played_beatmaps_scraping_limit.grid(row=1, column=0, pady=(0, 20))

            entry_start_rank = customtkinter.CTkEntry(App.frames['f2'], width=250, placeholder_text= "Starting Rank")
            entry_start_rank.grid(row=2, column=0, pady=(0, 20))

            entry_end_rank = customtkinter.CTkEntry(App.frames['f2'], width=250, placeholder_text="Ending Rank")
            entry_end_rank.grid(row=3, column=0, pady=(0, 20))

            entry_playstyle_scraping_limit = customtkinter.CTkEntry(App.frames['f2'], width=250, placeholder_text="Playstyle Scraping Limit")
            entry_playstyle_scraping_limit.grid(row=4, column=0, pady=(0, 20))

            def set_inputs():
                top_played_beatmaps_scraping_limit = int(entry_top_played_beatmaps_scraping_limit.get())
                starting_rank = int(entry_start_rank.get())
                ending_rank = int(entry_end_rank.get())
                if top_played_beatmaps_scraping_limit < 1 :
                    messagebox.showerror("Error", "Invalid Scraping Limit!")
                elif starting_rank < 1:
                    messagebox.showerror("Error", "Invalid Starting Rank!")
                elif top_played_beatmaps_scraping_limit < 1 and starting_rank < 1 : 
                    messagebox.showerror("Error", "Invalid Scraping Limit and Starting Rank!")

            
            enter_button = customtkinter.CTkButton(App.frames['f2'], text = "Enter", command=set_inputs)
            enter_button.grid(row=5, column=0)

            def label_button_frame_event(item):
                print(f"label button frame clicked: {item}")


            class ScrollableMentorFrame(customtkinter.CTkScrollableFrame):
                def __init__(self, master, command=None, **kwargs):
                    super().__init__(master, **kwargs)

                    self.command = command
                    self.radiobutton_variable = customtkinter.StringVar()
                    self.username_list = []
                    self.button_list = []
                    self.similarity_scores =[]

                def add_mentor(self, username, similarity_score, pfp=None):
                    username_label = customtkinter.CTkLabel(self, text=username, image=pfp, compound="left", padx=5, anchor="w")
                    button = customtkinter.CTkButton(self, text="See Profile", width=100, height=24)
                    similarity_label = customtkinter.CTkLabel(self, text=similarity_score, padx=20, anchor="e")
                    if self.command is not None:
                        button.configure(command=lambda: self.command(username))
                    username_label.grid(row=len(self.username_list), column=0, pady=(0, 20), sticky="w")
                    similarity_label.grid(row=len(self.similarity_scores), column=1, pady=(0, 20), sticky="e")
                    button.grid(row=len(self.button_list), column=2, pady=(0, 20), padx=10)
                    self.username_list.append(username_label)
                    self.similarity_scores.append(similarity_label)
                    self.button_list.append(button)

            scrollable_mentor_frame = ScrollableMentorFrame(master=App.frames['f2'], width=1250, command=label_button_frame_event, corner_radius=0)
            scrollable_mentor_frame.grid(row=0, rowspan=5, column=1, padx=40, pady=0, sticky="nsew")

            for i in range(20):  # add items with images
                scrollable_mentor_frame.add_mentor(f"Username {i}", f"Similarity Score: {i}", pfp=None)

            



        Login()
       


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()
    
