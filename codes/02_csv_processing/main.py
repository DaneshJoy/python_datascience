import os
import pandas as pd
from utils import calculate_bmi

# Should run this line for colors to work in CMD
os.system('cls')

# %% Part 1 - Load Data

# Read Data
data = pd.read_csv("data/hw_200.csv")

# Get Columns
# Method 1
heights = data["Height(Inches)"]
weights = data["Weight(Pounds)"]

# # Method 2
# heights = data.iloc[:, 1]
# weights = data.iloc[:, 2]

# %% Part 2 - Process Data

# Convert from Imperial to Metric
heights_metric = heights * 2.54
weights_metric = weights / 2.205

# Calculate BMI
calculated_bmis = []
# Method 1
for i in range(len(heights_metric)):
    bmi = calculate_bmi(heights_metric[i], weights_metric[i])
    calculated_bmis.append(bmi)

# # Method 2
# for hh, ww in zip(heights_metric, weights_metric):
#     calculated_bmis.append(calculate_bmi(hh, ww))

# %% Save Results
heights_metric = [round(i, 1) for i in heights_metric]
weights_metric = [round(i, 1) for i in weights_metric]

# 1- Convert lists to dictionary
result_dict = {"Height": heights_metric,
               "Weight": weights_metric,
               "BMI": calculated_bmis}

# 2- Convert dictionary to Pandas DataFrame
df_out = pd.DataFrame(result_dict)
print(df_out.describe())

# Report for Pandas Series
bmis = df_out['BMI']
print(f'\033[32m BMI max: \033[36m {bmis.max()} \033[0m')
print(f'\033[32m BMI min: \033[36m {bmis.min()} \033[0m')
print(f'\033[32m BMI average: \033[36m {bmis.mean():0.2f} \033[0m')


# 3- Save to file
out_path = 'results/test1'
if not os.path.exists(out_path):
    os.makedirs(out_path)

df_out.to_excel(f'{out_path}/result.xlsx')
df_out.to_csv(f'{out_path}/result.csv')
df_out.to_html(f'{out_path}/result.html')
df_out.to_json(f'{out_path}/result.json', indent=4)

