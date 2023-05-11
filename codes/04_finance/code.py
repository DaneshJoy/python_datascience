import pandas as pd
import mplfinance as mpf

# Load data from csv file
df = pd.read_csv('bitcoin_price_history.csv')

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# Remove commas from numerical columns
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['Open'] = df['Open'].str.replace(',', '').astype(float)
df['High'] = df['High'].str.replace(',', '').astype(float)
df['Low'] = df['Low'].str.replace(',', '').astype(float)

# Set date column as index
df.set_index('Date', inplace=True)

# Plot OHLC chart
mpf.plot(df, type='candle', style='charles', title='Bitcoin Price History')