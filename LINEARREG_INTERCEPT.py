import pandas as pd
import talib

output = talib.LINEARREG_INTERCEPT(data['F']['Close'].values)
import matplotlib.pyplot as plt

plt.plot(data['F']['Close'].values)
plt.plot(output)
