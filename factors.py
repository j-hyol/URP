import talib

def overlapStudies(open_, high, low, close, volume):
    # Bollinger Bands
    bbands = talib.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    # Double Exponential Moving Average
    dema = talib.DEMA(close, timeperiod=30)
    # Exponential Moving Average
    ema = talib.EMA(close, timeperiod=30)
    # Hilbert Transform - Instantaneous Trendline
    ht_trendline = talib.HT_TRENDLINE(close)
    # Kaufman Adaptive Moving Average
    kama = talib.KAMA(close, timeperiod=30)
    # Moving average
    ma = talib.MA(close, timeperiod=30, matype=0)
    # MESA Adaptive Moving Average
    mama = talib.MAMA(close, fastlimit=0, slowlimit=0)
    # Moving average with variable period
    mavp = talib.MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
    # MidPoint over period
    midpoint = talib.MIDPOINT(close, timeperiod=14)
    # Midpoint Price over period
    midprice = talib.MIDPRICE(high, low, timeperiod=14)
    # Parabolic SAR
    sar = talib.SAR(high, low, acceleration=0, maximum=0)
    # Parabolic SAR - Extended
    sarext = talib.SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    # Simple Moving Average
    sma = talib.SMA(close, timeperiod=30)
    # Triple Exponential Moving Average 
    t3 = talib.T3(close, timeperiod=5, vfactor=0)
    # Triple Exponential Moving Average
    tema = talib.TEMA(close, timeperiod=30)
    # Triangular Moving Average
    trima = talib.TRIMA(close, timeperiod=30)
    # Weighted Moving Average
    wma = talib.WMA(close, timeperiod=30)
    
    return bbands, dema, ema, ht_trendline, kama, ma, mama, mavp, midpoint, midprice, sar, sarext, sma, t3, tema, trima, wma

def statisticFunctions(open_, high, low, close, volume):
    # Beta
    beta = talib.BETA(high, low, timeperiod=5)
    # Pearson's Correlation Coefficient
    correl = talib.CORREL(high, low, timeperiod=30)
    # Linear Regression
    linearreg = talib.LINEARREG(close, timeperiod=14)
    # Linear Regression Angle
    linearreg_angle = talib.LINEARREG_ANGLE(close, timeperiod=14)
    # Linear Regression Intercept
    linearreg_intercept = talib.LINEARREG_INTERCEPT(close, timeperiod=14)
    # Linear Regression Slope
    linearreg_slope = talib.LINEARREG_SLOPE(close, timeperiod=14)
    # Standard Deviation
    stddev = talib.STDDEV(close, timeperiod=5, nbdev=1)
    # Time Series Forecast
    tsf = talib.TSF(close, timeperiod=14)
    # Variance
    var = talib.VAR(close, timeperiod=5, nbdev=1)
    
    return beta, correl, linearreg, linearreg_angle, linearreg_intercept, linearreg_slope, stddev, tsf, var
