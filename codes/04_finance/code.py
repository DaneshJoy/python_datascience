import pandas as pd
import mplfinance as mpf

# Load data from csv file
df = pd.read_csv('ETH-USD.csv')

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# Set date column as index
df.set_index('Date', inplace=True)

# Plot OHLC chart
mpf.plot(df, type='candle', style='charles', title='Etherium Price History')