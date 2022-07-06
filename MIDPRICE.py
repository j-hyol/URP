import yfinance as yf
import pandas as pd

df = pd.read_excel('(N=30 _ Freq=1D) Historical Data-GSON.xlsx')

symbol = 'F'
high = data[f'{symbol}']['High'].values
low = data[f'{symbol}']['Low'].values
output = talib.MIDPRICE(high, low)

plt.plot(high)
plt.plot(low)
plt.plot(output)
