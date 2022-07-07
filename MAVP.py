import yfinance as yf
import pandas as pd
import numpy as np

df = pd.read_excel('(N=30 _ Freq=1D) Historical Data-GSON.xlsx')

#data.reset_index(drop=False,inplace=True) #이거 없이 해도 바로 되는지 의문임

input_val = data[f'{symbol}']['Close'].values
periods = data.Date
real = talib.MAVP(input_val, periods, minperiod=2, maxperiod=30, matype=talib.MA_Type.T3)

plt.plot(input_val)
plt.plot(real)
