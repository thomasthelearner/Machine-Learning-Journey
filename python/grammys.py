# Write code below 💖
# List of songs with their durations (in minutes)
from functools import reduce

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
accumulator = 0

def min_to_sec(playlist):
  duration = playlist[1]
  minutes = int(duration)
  seconds = (duration - minutes)*100

  total_seconds = minutes*60 + round(seconds)
  return total_seconds

minutes_to_seconds = map(min_to_sec, playlist)
print(list(minutes_to_seconds))

def songs_longer_than_5min(playlist):
  return playlist[1] > 5

longer_than_5_minutes = filter(songs_longer_than_5min, playlist)
print(list(longer_than_5_minutes))

def total_duration(accumulator, playlist):
    return accumulator + playlist[1]

total = reduce(total_duration, playlist, 0)
print(total)
