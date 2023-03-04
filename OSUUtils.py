from ossapi import Ossapi, GameMode, UserLookupKey, RankingType, UserBeatmapType, Scope


class Utils():
    def __init__(self, api):
        self.api = api
        self.beatmap_details = {
        }
    
    def list_top_players(self, starting_rank, ending_rank, beatmap):
        scores = self.api.beatmap_scores(beatmap.id).scores
        for i in range(starting_rank - 1, ending_rank):
            score = scores[i]
            print(score.user().username)
    
    """
    Returns the top ten usernames of a beatmap.
    """
    def store_top_players(self,starting_rank, ending_rank, beatmap):
        scores = self.api.beatmap_scores(beatmap.id).scores
        top_ten_users = []
        for i in range(starting_rank - 1, ending_rank):
            score = scores[i]
            top_ten_users.append(score.user())

        
        return top_ten_users



    def get_top_ten_beatmapsets(self, user):
        # API stupidly returns a list of BeatmapPlaycount classes, rather than beatmap sets for most played beatmaps

        # Maybe cache this so it doesn't have to be called again, or put it into a function?????
        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=10)

        top_ten_beatmapsets = []

        for beatmap_play_count in beatmap_play_counts:
            # create a beatmapset object for all beatmaps in users top 10 played.
            # Expand each to scrape optional fields like genre, tags, ratings, etc. https://osu.ppy.sh/docs/index.html#beatmapsetcompact
            # The expand call takes a lot of time
            beatmapset = beatmap_play_count.beatmapset.expand()


            top_ten_beatmapsets.append(beatmapset)
            

            # self.store_beatmap_details(str(beatmapset).split(","))

        return top_ten_beatmapsets

    def get_top_ten_beatmaps(self, user):

        beatmap_play_counts = self.api.user_beatmaps(user.id, type=UserBeatmapType.MOST_PLAYED, limit=10)
        top_ten_beatmaps = []

        for beatmap_play_count in beatmap_play_counts:
            beatmap = beatmap_play_count.beatmap()
            top_ten_beatmaps.append(beatmap)
            # self.store_beatmap_details(beatmap)

        #self.get_average_difficulty(top_ten_beatmaps)

        return top_ten_beatmaps

    def get_average_difficulty(self, top_ten_beatmaps):
        difficulty_list = []
        for i in top_ten_beatmaps:
            beatmap_string = str(i).split(",")
            difficulty_list.append(float(beatmap_string[1][len(beatmap_string[1]) - 3: len(beatmap_string[1])]))

        print(difficulty_list)
        print(sum(difficulty_list) / len(difficulty_list))
        return (sum(difficulty_list) / len(difficulty_list))

    def get_common_beatmap_details(self, top_beatmap):
        
        for beatmap in top_beatmap:
            top_players = self.store_top_players(1, 10, beatmap)
        
            for players in top_players:
                genre = 0
                language = 0
                difficulty = 0
                length = 0
                bpm = 0
                circle_count = 0 
                slider_count = 0
                spinner_count = 0

                top_ten_beatmaps = self.get_top_ten_beatmaps(players)
                top_ten_beatmapsets = self.get_top_ten_beatmapsets(players)

                for beatmaps in range(len(top_ten_beatmapsets)):
                    
                    # expandedVariant = top_ten_beatmaps[beatmaps].expand()
                    
                    genre += (int(str(top_ten_beatmapsets[beatmaps].genre)[7]))
                    language += (int(str(top_ten_beatmapsets[beatmaps].language)[7]))
                    difficulty += (top_ten_beatmaps[beatmaps].difficulty_rating)
                    length += (top_ten_beatmaps[beatmaps].total_length)

                    # bpm += (expandedVariant.bpm)
                    # circle_count += (expandedVariant.count_circles)
                    # slider_count += (expandedVariant.count_sliders)
                    # spinner_count += (expandedVariant.count_spinners)
                    
                
                """
                The following commented out block of code gives the output in format of : 
                USERNAME : [value, value, value, value]

                The one after it provides it in: 
                USERNAME : {VALUE_TYPE : VALUE, VALUE_TYPE: VALUE, VALUE_TYPE: VALUE}

                CTRL + / TO UNCOMMENT C:
                """
                # self.beatmap_details[str(players.username)] = []
                # self.beatmap_details[str(players.username)].append(genre / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(language / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(difficulty / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(length / len(top_ten_beatmapsets))

                # self.beatmap_details[str(players.username)].append(bpm / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(circle_count / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(slider_count / len(top_ten_beatmapsets))
                # self.beatmap_details[str(players.username)].append(spinner_count / len(top_ten_beatmapsets))

                self.beatmap_details[str(players.username)] = {}
                self.beatmap_details[str(players.username)]["Genre: "] = (genre / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Language: "] = (language / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Difficulty: "] = (difficulty / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Length: "] = (length / len(top_ten_beatmapsets))

                self.beatmap_details[str(players.username)]["BPM: "] = (bpm / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Circle Count: "] = (circle_count / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Slider Count: "] = (slider_count / len(top_ten_beatmapsets))
                self.beatmap_details[str(players.username)]["Spinner Count: "] = (spinner_count / len(top_ten_beatmapsets))

                
                

        print(self.beatmap_details)
        
        
        



    def store_beatmap_details(self, beatMap):
        # self.beatmap_details["difficulty"].append(beatMap[28])
        # self.beatmap_details["length"].append(beatMap[32])
        # print(beatMap.index(" language={'id': 3", " 'name': 'Japanese'}"))
        counter = 0
        languageBool = False
        diffBool = False
        lengthBool = False
        genreBool = False

        print(beatMap.beatmap_attributes)
            # if i.__contains__("language=") and not languageBool:
            #     self.beatmap_details["language"].append(beatMap[counter][-1])
            #     languageBool = True
            # if i.__contains__("difficulty") and not diffBool:
            #     self.beatmap_details["difficulty"].append(beatMap[counter][-1])
            #     diffBool = True
            # if i.__contains__("total_length") and not lengthBool:
            #     self.beatmap_details["length"].append(beatMap[counter][14:-1])
            #     lengthBool = True
            # if i.__contains__("genre") and not genreBool:
            #     self.beatmap_details["genre"].append(beatMap[counter][-1])
            #     genreBool = True
            # counter += 1

        # print(beatMap)
