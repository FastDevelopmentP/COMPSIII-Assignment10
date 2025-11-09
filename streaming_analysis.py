import requests
from bs4 import BeautifulSoup
import sqlite3
import re
from word2number import w2n

import pandas as pd

df = pd.read_csv('streaming_data.csv')

print(df) 

completion_rate = df['completion_rate'].mean().round(2)
print(f"Average Completion Rate: {completion_rate}%")

total_time = df['duration_seconds'].sum() / 60
print(f"Total Time Spent Streaming: {total_time} minutes")

top_artists = df['artist'].value_counts().head(5)
print(f"Top 5 Artists:\n{top_artists}")

top_songs = df['song'].value_counts().head(10)
print(f"Top 10 Songs:\n{top_songs}")

top_genres = df['genre'].value_counts().head(5)
print(f"Top 5 Genres:\n{top_genres}")


query = "SELECT * FROM streaming_data;"