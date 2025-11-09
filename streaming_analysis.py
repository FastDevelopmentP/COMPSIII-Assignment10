import requests
from bs4 import BeautifulSoup
import sqlite3
import re
from word2number import w2n
import matplotlib.pyplot as plt

import pandas as pd

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 

df = pd.read_csv('streaming_data.csv')

# Convert month and day columns to Categorical with custom ordering 
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True) 
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True) 

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

days = df['day_of_week'].value_counts().sort_index()
print(f"Amount of songs listened to by Day of the Week:\n{days}")

month = df['month'].value_counts().sort_index()
print(f"Amount of songs listened to by Month:\n{month}")


# 1) Bar chart: songs by day
plt.figure()
days.plot(kind='bar')
plt.title('Songs Listened by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('songs_by_day.png')
plt.close()

# 2) Line chart: songs by month
plt.figure()
month.plot(kind='line')
plt.title('Songs Listened by Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('songs_by_month.png')
plt.close()

# 3) Histogram: duration in seconds
plt.figure()
df['duration_seconds'].plot(kind='hist')
plt.title('Duration of Songs Streamed in seconds')
plt.xlabel('Seconds')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('duration_histogram.png')
plt.close()