import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
  songs_df = pd.read_csv(file_path)
  return songs_df

def user_input():
  #greet user first with print statement
  print("Hello! Welcome to BeatRun. This program aims to help combine runners' music preferences, stride length, and speed they want to run and match those to songs from our database. BeatRun will make a playlist with songs that fit based on the user criteria and songs' beats per minute (BPM).")

  #have user input genre of choice
  genre_list = ["pop", "rock", "country", "R&B", "Dance/Electronic", "hip hop", "metal", "Folk/Acoustic", "latin", "easy listening", "blues", "World/Traditional"]
  genre = input("Please select one of the following music genres: pop, rock, country, R&B, Dance/Electronic, hip hop, metal, Folk/Acoustic, latin, easy listening, blues, World/Traditional")
  
  #while statement here to check if user input a valid response; if not, redo the input statement
  while True:
    if genre in genre_list:
      break
    else:
      print("Invalid genre. Please input one from the genre options.")
      genre = input("Please select one of the following music genres: pop, rock, country, R&B, Dance/Electronic, hip hop, metal, Folk/Acoustic, latin, easy listening, blues, World/Traditional")
  
  stride = input("Please input your stride length in feet (ex. 3.5).")
  #converting to float
  stride = float(stride)

  speed = input("Please the speed you want to run in miles per hour (ex. 6.3)")
  #converting to float
  speed = float(speed)

  return genre, stride, speed

def data_filter(genre, stride, speed, song_df):
  #converting stride/speed input into useable figure for dataset
  #formula: mph = (bpm * stride * 60) / 5280
  beats = ((speed * 5280) / 60) / stride
  
  #conditionals to filter songs_df to only the songs that closely fit the requirements of the user
  playlist_df = song_df[(song_df.genre.str.contains(genre)) & (song_df.tempo >= (beats-15)) & (song_df.tempo <= (beats+15))]

  return playlist_df

def final_playlist(playlist_df):
  #check if the playlist has any songs to present
  if len(playlist_df) > 0:
    #introduce data 
    print("Here's your playlist!")
  
    #iterate through filtered data frame and print the song name/artist for each song
    for i in range(len(playlist_df)):
      title = playlist_df.song.iloc[i]
      artist = playlist_df.artist.iloc[i]
      print(title, "by", artist)
  else:
    print("Sorry! Your criteria did not produce any matching songs. You can try again with a different speed or genre if you'd like!")

def playlist_stats(playlist_df):
  #taking averages of interesting stats from playlist dataframe and 
  #turning them into visually represented data to add to user experience
  popularity = playlist_df.popularity.mean()
  tempo = playlist_df.tempo.mean()

  #these measures are multiplied to put them on the same scale (out of 100) as popularity so bar plot is cleaner
  danceability = playlist_df.danceability.mean() * 100
  energy = playlist_df.energy.mean() * 100
  loudness = playlist_df.loudness.mean() * -10

  #setting up x and y axes for bar plot
  stats_list = ["popularity", "danceability", "energy", "loudness"]
  avg_stats = [popularity, danceability, energy, loudness]

  #checking if there are songs in playlist, printing nothing if 0 songs
  if len(playlist_df) > 0:
    print(f"The mean popularity of your playlist is {popularity:0.2f}. The mean danceability is {danceability:0.2f}, the mean energy is {energy:0.2f}, and the mean loudness is {loudness:0.2f}. If you want to find more songs that fit your speed/stride, the mean tempo is {tempo:0.2f} BPM. Thanks for using BeatRun!")
    
    #plotting characteristic stats visually
    plt.bar(stats_list, avg_stats)
    plt.xlabel('Song Characteristics')
    plt.ylabel('Averages')
    plt.title('Averages of Characteristics of Songs in Your Playlist')
    plt.show()
  else:
    print("")

def main():
  song_path = "~/Downloads/songs_normalize.csv"
  songs_df = read_csv(song_path)

  genre, stride, speed = user_input()
  
  playlist_df = data_filter(genre, stride, speed, songs_df)
  
  output = final_playlist(playlist_df)

  playlist_stats(playlist_df)

if __name__ == "__main__":
  main()
  
    
  
