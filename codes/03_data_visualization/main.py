import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('QueryResults.csv', header=0,
                 names=['DATE', 'TAG', 'POSTS'])

print(df.head())
print(df.tail())
print(df.shape)

print(df.groupby('TAG').sum())
print(df.groupby('TAG').count())

df.DATE = pd.to_datetime(df.DATE)
print(df.head())

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
                        'Power': [100, 80, 25, 50, 99, 75, 5]})
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)