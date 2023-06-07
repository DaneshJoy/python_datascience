import pandas as pd
from utils import print_df_info
import matplotlib.pyplot as plt


# data_path = r'D:\JD_Sharif\Python\Python_DataScience\github\codes\03_data_visualization\QueryResults.csv'
data_path = '../QueryResults.csv'
df = pd.read_csv(data_path,
                 names=['DATE', 'TAG', 'POSTS'],
                 header=0)

print_df_info(df)
# %% Data Pre-processing

print(df.groupby('TAG').sum())
df["DATE"] = pd.to_datetime(df["DATE"])

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

print_df_info(reshaped_df)

print('nan exists:', reshaped_df.isna().values.any())
reshaped_df.fillna(0, inplace=True)
print('nan exists:', reshaped_df.isna().values.any())

roll_df = reshaped_df.rolling(window=16).mean()

# %% Visualization

cpp = reshaped_df['c++']
swift = reshaped_df['swift']

plt.figure(figsize=(10, 7))
plt.plot(reshaped_df.index, cpp, label='C++')
plt.plot(swift, label='Swift')
plt.title('Trends')
plt.legend()
plt.show()

# %% Visualize all

plt.figure(figsize=(12,8))

for col in roll_df.columns:
    plt.plot(roll_df[col], label=col)

plt.legend(fontsize=16)
plt.xlabel('Date')
plt.ylabel('No. of Posts')








