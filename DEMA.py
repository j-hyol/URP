df = pd.read_excel('(N=30 _ Freq=1D) Historical Data-GSON.xlsx')

symbol = 'F'
input_val = data[f'{symbol}']['Close'].values
real = talib.DEMA(input_val, timeperiod=30)

plt.plot(input_val)
plt.plot(real)
