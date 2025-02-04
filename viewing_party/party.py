#------------------------------------------------
# THESE ARE DEFINED HELPER FUNCTIONS FOR WAVE 3+#
#------------------------------------------------

import collections

def generate_user_dict(user_info,dict_key): #makes the dict of user watched movies
    a_dict={entry["title"]:entry for entry in user_info[dict_key]}
    #for entry in user_info[dict_key]:
        #a_dict[entry["title"]]=entry
    return a_dict
def generate_friends_dict(user_info): #makes the dict of friend watched movies
    a_dict={entry["title"]:entry for count in user_info["friends"] for entry in count["watched"]}
    #for count in user_info["friends"]:
        #for entry in count["watched"]:
            #a_dict[entry["title"]]=entry
    return a_dict
def make_set_from_dict_keys(a_dict): #makes a set of movie titles from keys of movie list
    return set(key for key in a_dict.keys())
def list_dif_of_p1(set1, set2): #finds dif of s1 s2
    return list(set1.difference(set2))
def generate_movie_list(title_list,title_dict):
    return [title_dict[title] for title in title_list]
def set_comparison_from_data(dataset,user_subscript,userORfriend):
    dict1=generate_user_dict(dataset,user_subscript)
    dict2=generate_friends_dict(dataset)
    set1=make_set_from_dict_keys(dict1)
    set2=make_set_from_dict_keys(dict2)
    if userORfriend=="user":
        title_list=list_dif_of_p1(set1,set2)
        return (title_list, dict1)
    elif userORfriend=="friend":
        title_list=list_dif_of_p1(set2,set1)
        return (title_list, dict2)
    else:
        raise Exception ("you must choose user or friend")

# WAVE 1 START #

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        print("Missing title, genre or rating")
        return None
    movie_dict={
        "title":title,
        "genre":genre,
        "rating":rating
    }
    return movie_dict
def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for count in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][count]["title"]:
            user_data["watched"].append(user_data["watchlist"].pop(count))
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

print("Hello World!")
def get_watched_avg_rating(user_data):
    sum=0.0
    if len(user_data["watched"])<1:
        return sum
    for entry in user_data["watched"]:
        sum+=entry["rating"]
    return sum/len(user_data["watched"])
def get_most_watched_genre(user_data):
    if len(user_data["watched"])<1:
        return None
    genre_list=[]
    for entry in user_data["watched"]:
        genre_list.append(entry["genre"])
    counted=collections.Counter(genre_list)
    return counted.most_common()[0][0]




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    return generate_movie_list(*set_comparison_from_data(user_data,"watched","user"))
    
def get_friends_unique_watched(user_data):
    return generate_movie_list(*set_comparison_from_data(user_data,"watched","friend"))


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    (title_list, title_dict) = set_comparison_from_data(user_data,"watched","friend")
    user_subscriptions={entry for entry in user_data["subscriptions"]}
    movie_list=[]
    for title in title_list:
        if title_dict[title]["host"] in user_subscriptions:
            movie_list.append(title_dict[title])
    return movie_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    if not user_data["watched"]:
        return []
    (title_list, title_dict) = set_comparison_from_data(user_data,"watched","friend")
    user_genre_list=[entry["genre"] for entry in user_data["watched"]]
    user_preferred_genre=collections.Counter(user_genre_list).most_common()[0][0]
    return [title_dict[title] for title in title_list if title_dict[title]["genre"]==user_preferred_genre]

def get_rec_from_favorites(user_data):
    return generate_movie_list(*set_comparison_from_data(user_data,"favorites","user"))