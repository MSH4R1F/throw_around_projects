from Pymoe import Kitsu

#The clientid is the first paramter with the client password as the second
instance = Kitsu(username, password)
option = input("Anime:  ")

#anime.search searches through the kitsu list for the anime wanted
anime = instance.anime.search(option)
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(3):
    print("Showing top 3 results")
    title = anime[i]['attributes']['titles']['en_jp']
    synopsis = anime[i]['attributes']['synopsis']
    score = anime[i]['attributes']['averageRating']
    start_date = anime[i]['attributes']['startDate']
    end_date = anime[i]['attributes']['endDate']
    rank = anime[i]['attributes']['popularityRank']
    episode_count = anime[i]['attributes']['episodeCount']
    episode_length = anime[i]['attributes']['episodeLength']
    totalLength =  anime[i]['attributes']['totalLength']
    youtubeVideoId = anime[i]['attributes']['youtubeVideoId']
    url = anime[i]['attributes']["coverImage"]["original"]
    print(title)
    print("Summary: %s" %synopsis)
    print("Score: %s%%" %score)
    print("Start date: %s                    End date: %s" %(start_date, end_date))
    print("Episodes: %s                               Episode Length: %s" %(episode_count,episode_length))
    print("Trailer: https://www.youtube.com/watch?v=%s" % youtubeVideoId)
    print("Image: %s " % url)
    print("\n")
    print("-----------------------------------------------")

