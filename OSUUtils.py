from ossapi import *

class Utils():
    def __init__(self, api):
        self.api: Ossapi
        self.api = api
        self.beatmap_details = {
            "genre": [],
            "difficulty": [],
            "length": [],
            "language": []
        }

    def list_top_players(self, starting_rank, ending_rank, beatmap):
        scores = self.api.beatmap_scores(beatmap.id).scores
        for i in range(starting_rank - 1, ending_rank):
            try:
                score = scores[i]
                print(score.user().username)
            except IndexError:
                print("Empty List. Is this map graveyarded?")
                break


    def get_top_beatmapsets(self, user, limit):
        # API stupidly returns a list of BeatmapPlaycount classes, rather than beatmap sets for most played beatmaps
        
        # Maybe cache this so it doesn't have to be called again, or put it into a function?????
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=limit)
        
        top_beatmapsets = []

        for beatmap_play_count in beatmap_play_counts:
            # create a beatmapset object for all beatmaps in users top 10 played.
            # Expand each to scrape optional fields like genre, tags, ratings, etc. https://osu.ppy.sh/docs/index.html#beatmapsetcompact
            # The expand call takes a lot of time
            beatmapset = beatmap_play_count.beatmapset.expand()
            # self.store_beatmap_details(str(beatmapset).split(",")

            top_beatmapsets.append(beatmapset)

        return top_beatmapsets
    
    def get_top_beatmaps(self, user, limit):
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=limit)
        top_beatmaps = []

        for beatmap_play_count in beatmap_play_counts:
            beatmap = beatmap_play_count.beatmap()
            top_beatmaps.append(beatmap)

        return top_beatmaps

"""    def store_beatmap_details(self, beatMap):
        # self.beatmap_details["difficulty"].append(beatMap[28])
        # self.beatmap_details["length"].append(beatMap[32])
        # print(beatMap.index(" language={'id': 3", " 'name': 'Japanese'}"))
        counter = 0
        languageBool = False
        diffBool = False
        lengthBool = False
        genreBool = False
        for i in beatMap:
            if i.__contains__("language=") and not languageBool:
                self.beatmap_details["language"].append(beatMap[counter][-1])
                languageBool = True
            if i.__contains__("difficulty") and not diffBool:
                self.beatmap_details["difficulty"].append(beatMap[counter][-1])
                diffBool = True
            if i.__contains__("total_length") and not lengthBool:
                self.beatmap_details["length"].append(beatMap[counter][14:-1])
                lengthBool = True
            if i.__contains__("genre") and not genreBool:
                self.beatmap_details["genre"].append(beatMap[counter][-1])
                genreBool = True
            counter += 1

        print(self.beatmap_details)
        # beatMap.index("language =")
        # print(self.beatmap_details["length"])
        # print(self.beatmap_details["difficulty"])"""