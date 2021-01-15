'''

Technical_Test - Find average number of words by artist.

Finds the average number of words in songs by an artist.
If the names of 2 artists are passed then a comparison is performed.

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

if 2 <= numargs <= 3:
    artist_1 = sys.argv[1]
    if numargs == 3:
        artist_2 = sys.argv[2]
else:
    print("Invalid number of arguments passed.")
    quit()

def get_artist_id(artist):

  musicbrainzngs.set_useragent(app="technical_test", version=1.0, contact="none")

  artist = musicbrainzngs.search_artists(artist=artist_1)

  scores = []
  score = {}
  count = 0

# Obtain list of artists which match the name passed as a parameter
# There often several artists whose name matches - attempt to find the most popular one
# Sort the list and obtain the ID for the one with the biggest ext:score

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


# Obtain lyrics for a song and count the words

def get_lyrics(artist, title):
  r = requests.get("https://api.lyrics.ovh/v1/" + str(artist) + "/" + str(title) )
  if r.status_code != 200:
      return
  text=json.loads(r.text)
  lyrics=text["lyrics"]
  num_of_words = len(lyrics.split())
  if num_of_words > 0:
    #print(title)
    #print(num_of_words)
    global artist_songs
    global artist_words
    artist_songs+=1
    artist_words+=num_of_words

def get_tracks(artist, album):
    result = musicbrainzngs.search_releases(artist=artist, release=album, limit=1)
    id = result["release-list"][0]["id"]
    
    new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])
    t = (new_result["release"]["medium-list"][0]["track-list"])
    for x in range(len(t)):
        line = (t[x])
        get_lyrics(artist, line["recording"]["title"])
   
def get_song_length(artist_id):
  result = musicbrainzngs.get_artist_by_id(artist_id, includes=["release-groups"], release_type=["album"])
  for release_group in result["artist"]["release-group-list"]:
    get_tracks(artist_name, release_group["title"])
  
get_artist_id(sys.argv[1])

artist_songs = 0
artist_words = 0
artist_words_per_song = 0
get_song_length(artist_id)
if artist_songs != 0: 
  artist_words_per_song = artist_words / artist_songs

print("Artist " + artist_1 + "  -  " + str("{:.2f}".format(artist_words_per_song)) + " words per song")
print(str(artist_songs) + " Songs")
print(str(artist_words) + " Words")

if sys.argv[2] != ' ': 
  get_artist_id(sys.argv[2])

  artist_songs = 0
  artist_words = 0
  artist_words_per_song = 0
  get_song_length(artist_id)
  if artist_songs != 0: 
    artist_words_per_song = artist_words / artist_songs

  print("Artist " + artist_2 + "  -  " + str("{:.2f}".format(artist_words_per_song)) + " words per song")
 
  print(str(artist_songs) + " Songs")
  print(str(artist_words) + " Words")

#recordings = musicbrainzngs.search_works(arid=artist_id)
#print(recordings)

#for recobj in recordings["work-list"]:
#       print(recobj["title"])
 

'''

artis
ts = os.listdir("./files/")
results = [] ;
for artist in artists:
  tot_songs = 0
  tot_words = 0 
  songs = os.listdir("./files/" + artist )
  for song in songs:
    words = open("./files/" + artist + "/" + song )
    num_of_words = len(words.read().split())
    print("Song: " + song + " has " + str(num_of_words) + " words." )  
    tot_songs += 1
    tot_words += num_of_words
  tot_words=7
  average = "{:.3f}".format(tot_words / tot_songs)
  print(str(tot_words))
  #print(str("{:.4f}".format(average)))
  print("Artist: " + artist + " has " + str(tot_words / tot_songs) + " words per song." ) 
  result = {"Artist" : artist , "WordsPerSong" : average }
  results.append(result)
print(results)

class Vehicle:
  make = ' '
  model = ' '
  wheels = 0

class Car(Vehicle):
  def __init__(self, make, model):
    self.wheels = 2
    self.make = make
    self.model = model

  def change_wheels(self, wheels):
    self.wheels = wheels

mycar = Car(make="Vauxhall", model="Zafira")

print(mycar.wheels)
mycar.change_wheels(7)
print(mycar.wheels)

def Printout():
  global a
  a=1
  print('********')
Printout()

print("a=" + str(a))


'''



  




 
   