import my_package
import yfinance as yf
import matplotlib.pyplot as plt

def get_df(tickers, period):
    return yf.download(tickers, period=period)

# data=my_package.get_df("AAPL", "7d")
# print(data)

def plot_7d(df):
    plt.xlabel("Date")
    plt.ylabel("Close")
    return df['Close'].plot()

#my_package.plot_7d(data)

