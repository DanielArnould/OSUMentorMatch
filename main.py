from ossapi import *
import configparser
import OSUUtils
import GUI.py
from timeit import default_timer as timer

start = timer()

""""IMPORTANT NOTES:
Beatmap Set = All the associated beatmaps by an artist, for all difficulties, for a specific song.
Beatmap = A certain playmap for a certain difficulty in a beatmap set
Gamemode = OSU! actually contains 4 gamemodes, but the one which everyone knows is osu!standard or simply osu
Graveyarded beatmaps or beatmapsets don't contain any scores, but the api still returns an empty list.
Beatmaps in set are ordered from hardest difficulty to easiest difficulty
"""

# Client ID is needed for operation, client-secret allows for user control
# Create a new client at https://osu.ppy.sh/home/account/edit#oauth

config = configparser.RawConfigParser()
config.read('config.cfg')
keys_dict = dict(config.items('CONFIG'))

client_id = keys_dict['client_id']
client_secret = keys_dict['client_secret']


api = Ossapi(client_id, client_secret)
api.scopes = [Scope.PUBLIC, Scope.IDENTIFY]
user = api.user(user = keys_dict['user'], mode=GameMode.OSU)
utils = OSUUtils.Utils(api)

user_playstyle = utils.get_playstyle(user, scraping_limit=3)

# Looks at a user's top 10 played beatmaps, finds rank 1-4 players in each of them, gathers play style data based on their top 3 most played beatmaps
common_player_playstyles = utils.get_common_player_playstyles(user,
                                                        top_played_beatmaps_count=10, starting_rank=1,
                                                        ending_rank=3, playstyle_scraping_limit=3)

print(utils.get_playstyle_similarties(base_playstyle=user_playstyle, comparison_playstyles=common_player_playstyles))


end = timer()

print(f"Program took {end - start} secs to run")