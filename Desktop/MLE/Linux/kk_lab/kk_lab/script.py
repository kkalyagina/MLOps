import kk_lab
import yfinance as yf
import matplotlib.pyplot as plt

def avg_col(col_1, col_2, df):
    """
    Adding a new column with the average of the other two columns
    
    Parameters:
    ----------
    col_1 : str
        Valid col_1: Open, High, Low, Close, Adj Close, Volume
    col_2 : str
        Valid col_2: Open, High, Low, Close, Adj Close, Volume
    df : DataFrame
        Two-dimensional data structure
    
    Returns
    -------
    Union[dict, np.ndarray]
        One-dimensional ndarray
    """
    df['Avg'] = (df[col_1] + df[col_2]) / 2
    return df['Avg']

def get_df(tickers, period):
    """
    Download yahoo tickers
    
    Parameters:
    ----------
    tickers : str, list
        List of tickers to download
    period : str
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    
    Returns
    -------
    DataFrame
        Two-dimensional data structure with the additional column.
    """
    data=yf.download(tickers, period=period)
    data=data.assign(Avg=avg_col("High", "Low", data))
    return data

# data=my_package.get_df("AAPL", "7d")
# print(data)

def plot_7d(df, path):
    """
    Plotting and saving a graph
    
    Parameters:
    ----------
    df : indexable object, optional
        An object with labelled data. If given, provide the label names to plot in x and y.

    path : str or path-like
        A path to save the file
    
    Returns
    -------
    list of Line2D
        A list of lines representing the plotted data.
    """
    plt.xlabel("Date")
    plt.ylabel("Close")
    plot=df['Close'].plot()
    plt.savefig(path)
    return plot

#my_package.plot_7d(data, './apple.png')

