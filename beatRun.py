import pandas as pd

def read_csv(file_path):
  songs_df = pd.read_csv(file_path)
  return songs_df

def user_input():
  #greet user first with print statement
  print("Hello! Welcome to BeatRun. This program aims to help combine runners' music preferences, height, and speed they want to run and match those to songs from our database.BeatRun will make a playlist with songs that fit based on the user criteria and songs' beats per minute \(BPM\).")
  
  genre = input("Please select one of the following music genres: [GENRE OPTIONS]")
  #if statement here to check if user input a valid response; if not, redo the input statement
  if genre in genre_list:
    continue
  else:
    print("Invalid genre. Please input one from the genre options")
    genre = input("Please select one of the following music genres: [GENRE OPTIONS]")
  
  height = input("Please input your height in inches.")
  #if statement here to check if user input a valid response; if not, redo the input statement
  #what should the if statement look like?

  speed = input("Please the speed you want to run in miles per hour (ex. 6.3)")
  #if statement here to check if user input a valid response; if not, redo the input statement

  return genre, height, speed

def data_filter(genre, height, speed, song_df):
  #converting height/speed input into useable figure for dataset
  #would use if statements/math here likely 
  #beats = ___ 
  
  #conditionals to filter songs_df to only the songs that fit the requirements of the user
  playlist_df = songs_df[(songs_df.genre == genre) & (songs_df.beats == beats)]

  return playlist_df

def final_playlist(playlist_df):
  #introduce data 
  print("Here's your playlist!")
  
  #iterate through filtered data frame and print the song name/artist for each song
  for i in range(len(playlist_df)):
    title = playlist_df.title[i]
    artist = playlist_df.artist[i]
    print(title, "by", artist)

def main():
  song_path = "/Users/catelepinskas/Downloads/bcog200/final/music.csv"
  songs_df = read_csv(song_path)

  genre, height, speed = user_input()
  
  playlist_df = data_filter(genre, height, speed)
  
  output = final_playlist(playlist_df)

if __name__ == "__main__":
  main()
  
    
  
