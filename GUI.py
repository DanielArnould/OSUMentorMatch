import customtkinter
from tkinter import messagebox
from PIL import Image
import OSUUtils
from ossapi import *

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.login_label = customtkinter.CTkLabel(self, text="Login System", font=("Roboto", 24))
        self.login_label.pack(pady=12, padx=10)

        self.client_id_entry = customtkinter.CTkEntry(self, placeholder_text="Client ID", show="*")
        self.client_id_entry.pack(pady=12, padx=10)

        self.client_key_entry = customtkinter.CTkEntry(self, placeholder_text="Client Secret", show="*")
        self.client_key_entry.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="username")
        self.username_entry.pack(pady=12, padx=10)

        login_button = customtkinter.CTkButton(self, text="Login", command=login)
        login_button.pack(pady=12, padx=12)

        logo_image = customtkinter.CTkImage(Image.open("osuIconRevised.png"), size=(26, 26))

        # checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)

class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master, utils : OSUUtils.Utils, user : User):
        super().__init__(master, width=300, corner_radius=0)

        self.sidebar_label = customtkinter.CTkLabel(self, text="Sidebar!", font=("Roboto", 24))
        self.sidebar_label.grid(row=0, column=0, padx=90, pady=(20, 20))

        entry_top_played_beatmaps_scraping_limit = customtkinter.CTkEntry(self, width=250, placeholder_text="Top Played Beatmaps Scraping Limit")
        entry_top_played_beatmaps_scraping_limit.grid(row=1, column=0, pady=(0, 20))

        entry_start_rank = customtkinter.CTkEntry(self, width=250, placeholder_text= "Starting Rank")
        entry_start_rank.grid(row=2, column=0, pady=(0, 20))

        entry_end_rank = customtkinter.CTkEntry(self, width=250, placeholder_text="Ending Rank")
        entry_end_rank.grid(row=3, column=0, pady=(0, 20))

        entry_playstyle_scraping_limit = customtkinter.CTkEntry(self, width=250, placeholder_text="Playstyle Scraping Limit")
        entry_playstyle_scraping_limit.grid(row=4, column=0, pady=(0, 20))

        def set_inputs():
            try:
                top_played_beatmaps_scraping_limit = int(entry_top_played_beatmaps_scraping_limit.get())
                starting_rank = int(entry_start_rank.get())
                ending_rank = int(entry_end_rank.get())
                playstyle_scraping_limit = int(entry_playstyle_scraping_limit.get())

                user_playstyle = utils.get_playstyle(user, scraping_limit=top_played_beatmaps_scraping_limit)
                common_player_playstyles = utils.get_common_player_playstyles(user, top_played_beatmaps_count=top_played_beatmaps_scraping_limit, starting_rank=starting_rank, ending_rank=ending_rank, playstyle_scraping_limit=playstyle_scraping_limit)

                playstyle_similarties = utils.get_playstyle_similarties(base_playstyle=user_playstyle, comparison_playstyles=common_player_playstyles)
                
                def label_button_frame_event(item):
                    print(f"label button frame clicked: {item}")

                scrollable_mentor_frame = ScrollableMentorFrame(master=self, width=1250, command=label_button_frame_event, corner_radius=0)
                scrollable_mentor_frame.grid(row=0, rowspan=5, column=1, padx=40, pady=0, sticky="nsew")

                for mentor in playstyle_similarties:  
                    scrollable_mentor_frame.add_mentor(f"{mentor}", f"Similarity Score: {playstyle_similarties[mentor]}")

            except ValueError:
                messagebox.showerror("Error", "Invalid entry values")


        enter_button = customtkinter.CTkButton(self, text = "Enter", command=set_inputs)
        enter_button.grid(row=5, column=0)
    


        



class ScrollableMentorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.username_list = []
        self.button_list = []
        self.similarity_scores =[]

    def add_mentor(self, username, similarity_score):
        username_label = customtkinter.CTkLabel(self, text=username, compound="left", padx=5, anchor="w")
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





def login():
    print("Test")

