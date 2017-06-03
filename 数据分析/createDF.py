import pandas as pd

music_data = [("the rolling stones", "Satisfaction"), ("Beatles", "Let It Be"),
              ("Guns N'Roses", "Don't Cry"), ("Metallica", "Nothing Else Matters")]

table = pd.DataFrame(music_data)
table.index = range(1,5)
table.columns = ['singer','song_name']

print(table)