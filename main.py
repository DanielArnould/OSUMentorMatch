from ossapi import *
import configparser
import OSUUtils, GUI
from timeit import default_timer as timer
import customtkinter
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






















""""IMPORTANT NOTES:
Beatmap Set = All the associated beatmaps by an artist, for all difficulties, for a specific song.
Beatmap = A certain playmap for a certain difficulty in a beatmap set
Gamemode = OSU! actually contains 4 gamemodes, but the one which everyone knows is osu!standard or simply osu
Graveyarded beatmaps or beatmapsets don't contain any scores, but the api still returns an empty list.
Beatmaps in set are ordered from hardest difficulty to easiest difficulty
"""

# Client ID is needed for operation, client-secret allows for user control
# Create a new client at https://osu.ppy.sh/home/account/edit#oauth

# config = configparser.RawConfigParser()
# config.read('config.cfg')
# keys_dict = dict(config.items('CONFIG'))

# client_id = keys_dict['client_id']
# client_secret = keys_dict['client_secret']


# api = Ossapi(client_id, client_secret)
# api.scopes = [Scope.PUBLIC, Scope.IDENTIFY]
# user = api.user(user = keys_dict['user'], mode=GameMode.OSU)
# utils = OSUUtils.Utils(api)

# user_playstyle = utils.get_playstyle(user, scraping_limit=3)

# # Looks at a user's top 10 played beatmaps, finds rank 1-4 players in each of them, gathers play style data based on their top 3 most played beatmaps
# common_player_playstyles = utils.get_common_player_playstyles(user,
#                                                         top_played_beatmaps_count=10, starting_rank=1,
#                                                         ending_rank=3, playstyle_scraping_limit=3)

# print(utils.get_playstyle_similarties(base_playstyle=user_playstyle, comparison_playstyles=common_player_playstyles))


end = timer()

print(f"Program took {end - start} secs to run")