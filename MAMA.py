import pandas as pd
import talib

df = pd.read_excel('(N=30 _ Freq=1D) Historical Data-GSON.xlsx')

symbol = 'F'
input_val = data[f'{symbol}']['Close'].values
mama, fama = talib.MAMA(input_val)
import matplotlib.pyplot as plt

plt.plot(input_val)
plt.plot(mama)
plt.plot(fama)
