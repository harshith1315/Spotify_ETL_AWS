!pip install spotipy

!pip install python-dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# reading client id and client secret code
SPOTIPY_CLIENT_ID="60c5ee95e45b4d1e82891fa125b2f3f2"
SPOTIPY_CLIENT_SECRET="60c5ee95e45b4d1e82891fa125b2f3f2"

# connecting with spotify api
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# giving playlist link
playlist_code = input("Enter the Playlist Link: \n")
playlist_dict = sp.playlist(playlist_code)

no_of_songs = playlist_dict["tracks"]["total"]

album_list = []
song_list = []
release_date_list = []
artists_list = []

tracks = playlist_dict["tracks"]
items = tracks["items"]
offset=0
i=0
while i<no_of_songs:
    song = items[i-offset]["track"]["name"]
    album = items[i-offset]["track"]["album"]["name"]
    release_date = items[i-offset]["track"]["album"]["release_date"]
    artists = [k["name"] for k in items[i-offset]["track"]["artists"]]
    artists = ','.join(artists)
    album_list.append(album)
    song_list.append(song)
    release_date_list.append(release_date)
    artists_list.append(artists)
    if (i+1)%100 == 0:
        tracks = sp.next(tracks)
        items = tracks["items"]
        offset = i+1
    i+=1

final_data = list(zip(song_list,artists_list,album_list,release_date_list))


# creating csv file
import csv
Details = ["Name","Artists","Album","Release Date"]
rows = final_data
a=input("enter album name")
with open(a+".csv",'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(Details)
    write.writerows(rows)

f.close()
