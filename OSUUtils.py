from ossapi import *
from math import *
from statistics import mode, mean


class Utils():
    def __init__(self, api):
        self.api = api
        self.beatmap_details = {
        }
    

    def get_top_players(self, starting_rank, ending_rank, beatmap : Beatmap):
        scores = self.api.beatmap_scores(beatmap.id).scores
        top_players = []

        for rank in range(starting_rank - 1, ending_rank):
            try:
                score = scores[rank]
                top_players.append(score.user())
            except IndexError:
                print("Empty List. Is this map graveyarded?")
                break

        return top_players

    def get_top_played_beatmapsets(self, user, limit):
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=limit)
        
        top_beatmapsets = []

        for beatmap_play_count in beatmap_play_counts:
            # Expand each to scrape optional fields like genre, tags, ratings, etc. https://osu.ppy.sh/docs/index.html#beatmapsetcompact
            # The expand call takes a lot of time
            beatmapset = beatmap_play_count.beatmapset.expand()
            top_beatmapsets.append(beatmapset)

        return top_beatmapsets

    def get_top_played_beatmaps(self, user, limit):
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=limit)
        top_beatmaps = []

        for beatmap_play_count in beatmap_play_counts:
            beatmap = beatmap_play_count.beatmap().expand() #MUST EXTEND for circle count, spinner count, slider count, and BPM
            top_beatmaps.append(beatmap)

        return top_beatmaps
    
    def get_beatmapsets(self, beatmaps: list[Beatmap]):
        beatmapsets = []

        for beatmap in beatmaps:
            beatmapsets.append(beatmap.beatmapset())

        return beatmapsets


    def get_average_difficulty(self, beatmaps: list[Beatmap]):
        difficulty_ratings = []

        for beatmap in beatmaps:
            difficulty_ratings.append(beatmap.difficulty_rating)

        return mean(difficulty_ratings)
    

    def get_most_common_language_id(self, beatmapsets: list[Beatmapset]):
        language_ids = []

        for beatmapset in beatmapsets:
            language_ids.append(beatmapset.language['id'])

        return mode(language_ids)
    

    def get_most_common_genre_id(self, beatmapsets: list[Beatmapset]):
        genre_ids = []

        for beatmapset in beatmapsets:
            genre_ids.append(beatmapset.genre['id'])

        return mode(genre_ids)
    

    def get_average_length(self, beatmaps: list[Beatmap]):
        lengths = []

        for beatmap in beatmaps:
            lengths.append(beatmap.total_length)

        return mean(lengths)
    

    def get_average_bpm(self, beatmaps: list[Beatmap]):
        bpms = []

        for beatmap in beatmaps:
            bpms.append(beatmap.bpm)

        return mean(bpms)
    

    def get_average_circle_count(self, beatmaps: list[Beatmap]):
        circle_counts = []

        for beatmap in beatmaps:
            circle_counts.append(beatmap.count_circles)

        return mean(circle_counts)
    

    def get_average_slider_count(self, beatmaps: list[Beatmap]):
        slider_counts = []

        for beatmap in beatmaps:
            slider_counts.append(beatmap.count_sliders)

        return mean(slider_counts)
    

    def get_average_spinner_count(self, beatmaps: list[Beatmap]):
        spinner_counts = []

        for beatmap in beatmaps:
            spinner_counts.append(beatmap.count_spinners)

        return mean(spinner_counts)

    
    # limit -> How many beatmaps should be analysed from the user's top played beatmaps
    def get_playstyle(self, user, scraping_limit):
        top_beatmaps = self.get_top_played_beatmaps(user, scraping_limit)
        top_beatmapsets = self.get_top_played_beatmapsets(user, scraping_limit)
        
        average_difficulty = self.get_average_difficulty(top_beatmaps)
        most_common_language_id = self.get_most_common_language_id(top_beatmapsets)
        most_common_genre_id = self.get_most_common_genre_id(top_beatmapsets)
        average_length = self.get_average_length(top_beatmaps)

        # Require expansion of Beatmaps

        average_bpm = self.get_average_bpm(top_beatmaps)
        average_circle_count = self.get_average_circle_count(top_beatmaps)
        average_slider_count = self.get_average_slider_count(top_beatmaps)
        average_spinner_count = self.get_average_spinner_count(top_beatmaps)

        playstyle = {
            'Average Difficulty': average_difficulty,
            'Most Common Language Id': most_common_language_id,
            'Most Common Genre Id': most_common_genre_id,
            'Average Length': average_length,
            'Average BPM': average_bpm,
            'Average Circle Count': average_circle_count,
            'Average Slider Count': average_slider_count,
            'Average Spinner Count': average_spinner_count
        }

        return playstyle
    
    # limit -> How many beatmaps should be analysed from the player's top played beatmaps
    def get_playstyles(self, players : list[User], scraping_limit):
        playstyles = {}
        
        for player in players:
            playstyles[player.username] = self.get_playstyle(player, scraping_limit)

        return playstyles

    # Provides playstyles as USERNAME : {VALUE_TYPE : VALUE, VALUE_TYPE: VALUE, VALUE_TYPE: VALUE}
    def get_common_player_playstyles(self, user, top_played_beatmaps_count, starting_rank, ending_rank, playstyle_scraping_limit):
        top_played_beatmaps = self.get_top_played_beatmaps(user, limit=top_played_beatmaps_count)
        playstyles = {}
        for beatmap in top_played_beatmaps:
            top_players = self.get_top_players(starting_rank, ending_rank, beatmap)
            playstyles.update(self.get_playstyles(top_players, playstyle_scraping_limit))

        return playstyles


    def get_playstyle_similarity(self, playstyle1, playstyle2):

        # Calculates cosine similarity between vector representations of each playstyle

        # No need to worry about key matching because both lists are structured the same
        # No need to normalise since we aren't relying on distant metrics
        vector1 = list(playstyle1.values())
        vector2 = list(playstyle2.values())

        # Euclidean magnitude is always the square root of the sum of each vector element
        # think about finding the diagonal in a rectangular prism only with its side lengths
        magnitude1 = sqrt(sum(a * a for a in vector1))
        magnitude2 = sqrt(sum(a * a for a in vector2))

        # Finds the dot product between the two vectors
        # Remember dot produt = cosine similarity  * magnitude
        numerator = sum(a * b for a,b in zip(vector1,vector2))
        denominator = magnitude1 * magnitude2

        return round(numerator / denominator, 4)
    

    def get_playstyle_similarties(self, base_playstyle, comparison_playstyles):
        similarities = {}

        for username in comparison_playstyles:
            playstyle_similarity = self.get_playstyle_similarity(base_playstyle, comparison_playstyles[username])
            similarities.update({username : playstyle_similarity})

        return similarities