from Pymoe import Anilist
import pprint

instance = Anilist()

while True:
     option  = input("Anime or Manga:  ")
     option = option.upper()
     if option == "ANIME" or option == "MANGA":
        break
    

if option == "ANIME":
    option2 = input("Anime:   ")
    anime = instance.search.anime(option2)
    length = len(anime['data']['Page']['media'])
    print("%s results " %length)
    print("\n")
    print("\n")
    for i in range(len(anime['data']['Page']['media'])):
        print("Title(Romaji): %s" % anime['data']['Page']['media'][i]['title']['romaji'])
        print("Title(English): %s" % anime['data']['Page']['media'][i]['title']['english'])
        print("Score: %s%%" % anime['data']['Page']['media'][i]['averageScore'])
        print("Episodes: %s" % anime['data']['Page']['media'][i]['episodes'])
        print("Popularity: %s" % anime['data']['Page']['media'][i]['popularity'])
        print("Season: %s" % anime['data']['Page']['media'][i]['season'])
        print("-----------------------------------------------------------------")
        print(" ")
else:
    option2 = input("Manga: ")
    manga = instance.search.manga(option2)
    length = len(manga['data']['Page']['media'])
    print("%s results " %length)
    print("\n")
    print("\n")
    for i in range(len(manga['data']['Page']['media'])):
        print("Title(Romaji): %s" % manga['data']['Page']['media'][i]['title']['romaji'])
        print("Title(English): %s" % manga['data']['Page']['media'][i]['title']['english'])
        print("Score: %s%%" % manga['data']['Page']['media'][i]['averageScore'])
        print("Chapters: %s" % manga['data']['Page']['media'][i]['chapters'])
        print("Popularity: %s" % manga['data']['Page']['media'][i]['popularity'])
        print("-----------------------------------------------------------------")
        print(" ")
