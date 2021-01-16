'''

Technical_Test - Find average number of words by artist.

Finds the average number of words in songs by an artist.
The names of 2 artists can be passed for comparison.

Example Command: python Technical_Test_PDR.py "D" "Neil Young" "The Pixies"

The first parameter can be "D" or "S"
    D - Detailed report including retrieved song names and number of words
    S - Summary report with just average number number of words per song

Subsequent parameters have either one or two artists names.

Need to do 
pip install musicbrainxngs
pip install requests

'''

import os
import sys
import musicbrainzngs
import requests
from operator import itemgetter
import json

numargs = len(sys.argv)

if 3 <= numargs <= 4:
    artist_1 = sys.argv[2]
    if numargs == 4:
        artist_2 = sys.argv[3]
else:
    print("Invalid number of arguments passed.")
    quit()

if sys.argv[1] !="S" and sys.argv[1] !="D":
    print("First parameter has to be S or D")
    quit()

musicbrainzngs.set_useragent(app="technical_test", version=1.0, contact="none")

# Obtain list of artists which match the name passed as a parameter
# There often several artists whose name matches - attempt to find the most popular one
# Sort the list and obtain the ID for the one with the biggest ext:score

def get_artist_id(artist):

  artist = musicbrainzngs.search_artists(artist=artist)

  scores = []
  score = {}
  count = 0

  for obj in artist["artist-list"]:
    count+=1
    score["artist"] = obj["name"]
    score["id"] = obj["id"]
    score["score"] = obj["ext:score"]
    score["count"] = count
    scores.append(score.copy())
    
  scores.sort(key=(itemgetter("score")))

  first_dict=scores[0]
  global artist_id
  global artist_name
  artist_id=first_dict["id"]
  artist_name=first_dict["artist"]


# Obtain lyrics for a song and count the words and number of songs
# in global variables.

def get_lyrics(artist, title):
  r = requests.get("https://api.lyrics.ovh/v1/" + str(artist) + "/" + str(title) )
  if r.status_code != 200:
      return
  text=json.loads(r.text)
  lyrics=text["lyrics"]
  num_of_words = len(lyrics.split())
  if num_of_words > 0:
    if sys.argv[1] == "D":
        print(str(num_of_words) + " : " + title)
    global artist_songs
    global artist_words
    artist_songs+=1
    artist_words+=num_of_words


# Get track lists from albums identified

def get_tracks(artist, album):
    result = musicbrainzngs.search_releases(artist=artist, release=album, limit=1)
    id = result["release-list"][0]["id"]
    
    new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])
    t = (new_result["release"]["medium-list"][0]["track-list"])
    for x in range(len(t)):
        line = (t[x])
        get_lyrics(artist, line["recording"]["title"])


# Get average song length for an artist by identifying album releases
# then call other functions to get songs and lyrics.

def get_song_length(artist_id):
  result = musicbrainzngs.get_artist_by_id(artist_id, includes=["release-groups"], release_type=["album"])
  for release_group in result["artist"]["release-group-list"]:
    get_tracks(artist_name, release_group["title"])
  
get_artist_id(sys.argv[2])

artist_songs = 0
artist_words = 0
artist_words_per_song = 0
get_song_length(artist_id)
if artist_songs != 0: 
  artist_words_per_song = artist_words / artist_songs

print("Artist " + artist_1 + "  -  " + str("{:.2f}".format(artist_words_per_song)) + " words per song")
print(str(artist_songs) + " Songs")
print(str(artist_words) + " Words")

if numargs == 4:
  artist_id = " "
  get_artist_id(sys.argv[3])

  artist_songs = 0
  artist_words = 0
  artist_words_per_song = 0
  get_song_length(artist_id)
  if artist_songs != 0: 
    artist_words_per_song = artist_words / artist_songs

  print("Artist " + artist_2 + "  -  " + str("{:.2f}".format(artist_words_per_song)) + " words per song")
 
  print(str(artist_songs) + " Songs")
  print(str(artist_words) + " Words")




 
   