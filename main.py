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
top_beatmaps = utils.get_top_beatmaps(user, limit=10)

print(utils.get_most_common_genre_id(top_beatmapsets))
print(utils.get_most_common_language_id(top_beatmapsets))
print(utils.get_average_difficulty(top_beatmaps))
print(utils.get_average_length(top_beatmaps))
print(utils.get_average_bpm(top_beatmaps)) # NOT ALL MAPS HAVE BPM SPECIFIED
print(utils.get_average_circle_count(top_beatmaps))
print(utils.get_average_slider_count(top_beatmaps))
print(utils.get_average_spinner_count(top_beatmaps))

















"""for beatmapset in top_ten_beatmapsets:
    print(beatmapset.genre["name"])
    easiest_beatmap = beatmapset.beatmaps[0]
    scores = api.beatmap_scores(easiest_beatmap.id).scores
    print(len(scores))"""