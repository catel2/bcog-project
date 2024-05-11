import pytest
import pandas as pd
from beatRun import read_csv, user_input, data_filter, final_playlist

@pytest.fixture
def sample_songs_df():
  #making sample df to test
  sample_data = {'song':['Song 1', 'Song 2', 'Song 3'], 
                 'artist':['Artist 1', 'Artist 2', 'Artist 3'],
                 'genre':['rock', 'pop', 'hip hop'],
                 'tempo':[120, 140, 160]}
  df = pd.DataFrame(sample_data)
  
  return df

def test_read_csv():
  #testing read_csv
  songs_df = read_csv("~/Downloads/songs_normalize.csv")
  assert isinstance(songs_df, pd.DataFrame) #check

def test_user_input(monkeypatch):
  #testing user_input
  #mocking user input with monkeypatch
  mock_input_values = ['hip hop', '3.5', '6.3']
  monkeypatch.setattr('builtins.input', lambda _: mock_input_values.pop(0))
  genre, stride, speed = user_input()
  assert isinstance(genre, str)
  assert isinstance(stride, float)
  assert isinstance(speed, float)

def test_data_filter(sample_songs_df):
  #testing data_filter
  genre = 'hip hop'
  stride = 3.5
  speed = 6.3
  filtered_df = data_filter(genre, stride, speed, sample_songs_df)
  assert not filtered_df.empty

def test_final_playlist(capsys):
  #testing final_playlist
  sample_playlist_df = pd.DataFrame({
    'song': ['Song 1', 'Song 2'],
    'artist': ['Artist 1', 'Artist 2']})
  final_playlist(sample_playlist_df)
  captured = capsys.readouterr()
  assert "Here's your playlist!" in captured.out
  assert "Song 1 by Artist 1" in captured.out
  assert "Song 2 by Artist 2" in captured.out

