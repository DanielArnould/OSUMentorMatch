from ossapi import Ossapi, GameMode, UserLookupKey, RankingType, UserBeatmapType, Scope

class Utils():
    def __init__(self, api):
        self.api = api

    def list_top_players(self, starting_rank, ending_rank, beatmap):
        scores = self.api.beatmap_scores(beatmap.id).scores
        for i in range(starting_rank - 1, ending_rank):
            score = scores[i]
            print(score.user().username)


    def get_top_ten_beatmapsets(self, user):
        # API stupidly returns a list of BeatmapPlaycount classes, rather than beatmap sets for most played beatmaps
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=10)
        top_ten_beatmapsets = []

        for beatmap_play_count in beatmap_play_counts:
            # create a beatmapset object for all beatmaps in users top 10 played.
            # Expand each to scrape optional fields like genre, tags, ratings, etc. https://osu.ppy.sh/docs/index.html#beatmapsetcompact
            # The expand call takes a lot of time
            beatmapset = beatmap_play_count.beatmapset.expand()
            top_ten_beatmapsets.append(beatmapset)

        return top_ten_beatmapsets