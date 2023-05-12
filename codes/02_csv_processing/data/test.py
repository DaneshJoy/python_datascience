import pandas as pd

filepath = "weather_data.csv"

df = pd.read_csv(filepath)

t = df['temp']

c = df['condition']

print(df[df['condition'] == "Rain"])
