import asyncio
from ossapi import *
import configparser
import OSUUtils

""""IMPORTANT NOTES:
Beatmap Set = All the associated beatmaps by an artist, for all difficulties, for a specific song.
Beatmap = A certain playmap for a certain difficulty in a beatmap set
Gamemode = OSU! actually contains 4 gamemodes, but the one which everyone knows is osu!standard or simply osu
Graveyarded beatmaps or beatmapsets don't contain any scores, but the api still returns an empty list.
Beatmaps in set are ordered from hardest difficulty to easiest difficulty
"""

config = configparser.RawConfigParser()
config.read('config.cfg')
keys_dict = dict(config.items('CONFIG'))


# Client ID is needed for operation, client-secret allows for user control
# Create a new client at https://osu.ppy.sh/home/account/edit#oauth
client_id = keys_dict['client_id']
client_secret = keys_dict['client_secret']
api = Ossapi(client_id, client_secret)
user = api.user(user = keys_dict['user'], mode=GameMode.OSU)

utils = OSUUtils.Utils(api)
    
top_beatmapsets = utils.get_top_beatmapsets(user, limit=10)

for i in range(0, 10):
    utils.list_top_players(starting_rank=1, ending_rank=10, beatmap=top_beatmapsets[i].beatmaps[0])

















"""for beatmapset in top_ten_beatmapsets:
    print(beatmapset.genre["name"])
    easiest_beatmap = beatmapset.beatmaps[0]
    scores = api.beatmap_scores(easiest_beatmap.id).scores
    print(len(scores))"""