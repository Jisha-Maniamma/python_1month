# import demo
#
# albums=demo.albums

from demo import albums
SONG_INDEX=3
choice_album="-"

while choice_album!=0:

    ii = 0
    for album, artist, year, songs in albums:
        ii += 1
        print(ii, ": ", album)
    list_songs=[]
    choice_album=int(input("please chose your album "))
    songs=albums[choice_album-1][SONG_INDEX]

    for x, y in songs:
        print(x, ": ", y)
        list_songs.append(y)
    choice_song = int(input("choose your song"))
    if choice_song<len(list_songs):
        print(f"playing {list_songs[choice_song-1]}")
        print("*"*10)
    else:
        continue

