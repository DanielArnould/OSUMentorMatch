from ossapi import Ossapi, GameMode, UserLookupKey, RankingType, UserBeatmapType, Scope
# import configparser
import OSUUtils

""""IMPORTANT NOTES:
Beatmap Set = All the associated beatmaps by an artist, for all difficulties, for a specific song.
Beatmap = A certain playmap for a certain difficulty in a beatmap set
Gamemode = OSU! actually contains 4 gamemodes, but the one which everyone knows is osu!standard or simply osu
Graveyarded beatmaps or beatmapsets don't contain any scores, but the api still returns an empty list.
Beatmaps in set are ordered from hardest difficulty to easiest difficulty
"""

# config = configparser.RawConfigParser()
# config.read('config.cfg')
# keys_dict = dict(config.items('CONFIG'))

# Client ID is needed for operation, client-secret allows for user control
# Create a new client at https://osu.ppy.sh/home/account/edit#oauth
# client_id = keys_dict['client_id']
# client_secret = keys_dict['client_secret']

client_id = 20800
client_secret = "1CwngLGnXiBszeUcTuWyRpWzmWp3Itd7fErVEAhj"
userId = 9545422

api = Ossapi(client_id, client_secret)
api.scopes = [Scope.PUBLIC, Scope.IDENTIFY]
user = api.user(user = userId, mode=GameMode.OSU)
utils = OSUUtils.Utils(api)

top_ten_beatmapsets = utils.get_top_ten_beatmapsets(user)
first_beatmap = top_ten_beatmapsets[0].beatmaps[0]

# Each call of this function takes ~ 6-7 Seconds
utils.list_top_players(1, 10, first_beatmap)
utils.store_beatmap_details(first_beatmap)




"""for beatmapset in top_ten_beatmapsets:
    print(beatmapset.genre["name"])
    easiest_beatmap = beatmapset.beatmaps[0]
    scores = api.beatmap_scores(easiest_beatmap.id).scores
    print(len(scores))"""