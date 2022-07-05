import pandas as pd
import talib

df = pd.read_excel('(N=30 _ Freq=1D) Historical Data-GSON.xlsx')

symbol = 'F'
input_val = data[f'{symbol}']['Close'].values
output = talib.MA(input_val, matype=talib.MA_Type.T3)

plt.plot(input_val)
plt.plot(output)
