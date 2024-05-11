import pytest
import pandas as pd
from your_script import read_csv, user_input, data_filter, final_playlist

def sample_songs_df():
  #making sample df to test
  sample_data = {'title':['Song 1', 'Song 2', 'Song 3'], 
                 'artist':['Artist 1', 'Artist 2', 'Artist 3'],
                 'genre':['rock', 'pop', 'hip hop'],
                 'tempo':[120, 140, 160]}
  df = pd.DataFrame(sample_data)
  
  return df

def test_read_csv():
  #testing read_csv
  songs_df = read_csv("~/Downloads/songs_normalize.csv")
  assert isinstance(songs_df, pd.DataFrame) #check

