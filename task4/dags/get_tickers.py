# Airflow imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Date, Yahoo Finance, and Pandas
from datetime import timedelta, datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def download_market_data(ticker, **context):
    """
    Downloads market data for given ticker in 1h intervals
    
    Args: 
        ticker: ticker to download
    Returns: 
        None; Saves data as csv in working directory
    """

    # Download data and save as CSV
    print("CONTEXT", context)
    print(context['ds'])
    df = yf.download(ticker, start=pd.to_datetime(context['ds']), end=pd.to_datetime(context['ds'])+pd.DateOffset(1), interval = '1h')
    df.to_csv(f'{ticker}_data.csv', header = False)
    
def query_data(**kwargs):
    """
    Queries data for given ticker and outputs average for this ticker
    Args: 
        **kwargs: contains 'tickers' list and Airflow context variables
    Returns: 
        None; writes files to date-specific folders
    """

   # Get variables from kwargs, create empty dataframe with columns
    ds = kwargs['ds']
    tickers = kwargs['tickers']
    combined_df = pd.DataFrame()

    for ticker in tickers:

        # Load data, add ticker column, append to combined_df
        df = pd.read_csv(f'~/data/{ds}/{ticker}_data.csv', header = None)
        df[len(df.columns)] = f'{ticker}'
        combined_df = combined_df.append(df, ignore_index = True)
 
    # Set column names, add date column, round to 2 decimals
    combined_df.columns = ['date_time', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'ticker']
    combined_df['date'] = combined_df['date_time'].str[:10]
    combined_df = combined_df.round(2)

    # Calculate average value between high and low prices of ticker and write to CSV
    daily_agg_df=combined_df[['ticker', 'date', 'high', 'low']]
    daily_agg_df['Avg'] = (daily_agg_df['high'] + daily_agg_df['low']) / 2
    daily_agg_df.drop(['high','low'], inplace=True, axis=1)
    daily_agg_df.to_csv(f'~/data/{ds}/avg_data.csv')



def sma(**kwargs):
    """
    Calculate 5 SMA and 20 SMA
    
    Args: 
        **kwargs: contains 'tickers' list and Airflow context variables
    Returns: 
        None; writes files to date-specific folders
    """
    ds = kwargs['ds']
    tickers = kwargs['tickers']
    combined_df = pd.DataFrame()

    for ticker in tickers:

        # Load data, add ticker column, append to combined_df
        df = pd.read_csv(f'~/data/{ds}/avg_data.csv')
        df[len(df.columns)] = f'{ticker}'
        combined_df = combined_df.append(df, ignore_index = True)
    
    sma=combined_df[['ticker', 'date', 'Avg']]
    sma['sma_5']=sma['Avg'].rolling(window=5, min_periods=1, center=False).mean()
    sma['sma_20']=sma['Avg'].rolling(window=20, min_periods=1, center=False).mean()

    sma.to_csv(f'~/data/{ds}/sma_data.csv')
   


def plot(**kwargs):
    """
    Build plot
        
    Args: 
        **kwargs: contains 'tickers' list and Airflow context variables
    Returns: 
        None; writes files to date-specific folders
    """
    # Get variables from kwargs, create empty dataframe with columns
    ds = kwargs['ds']
    tickers = kwargs['tickers']
    combined_df = pd.DataFrame()

    for ticker in tickers:

        # Load data, add ticker column, append to combined_df
        df = pd.read_csv(f'~/data/{ds}/sma_data.csv')
        df[len(df.columns)] = f'{ticker}'
        combined_df = combined_df.append(df, ignore_index = True)
    
    graph=combined_df[['ticker', 'date', 'Avg', 'sma_5', 'sma_20']]
    
    #Build plot
    fig=plt.figure(figsize=(20,15))
    ax1=fig.add_subplot(ylabel=ticker)
    graph['Avg'].plot(ax=ax1, color='black')
    graph[['Avg', 'sma_5', 'sma_20']].plot(ax=ax1)
    plt.savefig(f'/usr/local/airflow/data/{ds}/plot_data.png')



# Set retries in default args
default_args = {
    #'start_date': datetime(2021, 4, 19),
    'retry_delay': timedelta(minutes = 5),
    'retries': 2
}

# Build dag
dag = DAG(
    'yahoo_finance_pipeline',
    default_args = default_args,
    description = 'A simple DAG using Yahoo Finance data',
    #schedule_interval = '0 17 * * *',
    schedule_interval=timedelta(1),
    start_date = datetime(2021, 4, 19),
    max_active_runs=1
)

# Initialize temp directory for data
t0 = BashOperator(
    task_id = 'init_temp_directory',
    bash_command = 'mkdir -p ~/data/{{ ds }}',
    dag = dag
)

# Download TSLA market data
t1 = PythonOperator(
    task_id = 'download_TSLA',
    python_callable = download_market_data,
    op_args = ['TSLA'], 
    provide_context=True,
    dag = dag
)

#Move TSLA to directory
t2 = BashOperator(
    task_id = 'move_TSLA',
    bash_command = 'mv ~/TSLA_data.csv ~/data/{{ ds }}',
    dag = dag
)

# Query data and output new file
t3 = PythonOperator(
    task_id = 'query_data',
    python_callable = query_data,
    op_kwargs = {'tickers': ['TSLA']},
    provide_context = True,
    dag = dag
)

# #Calculate SMA 5 and SMA 20 and save results 
t4 = PythonOperator(
    task_id = 'calculate_sma',
    python_callable = sma,
    op_kwargs = {'tickers': ['TSLA']},
    provide_context = True,
    dag = dag
)

t5 = PythonOperator(
    task_id = 'build_plot',
    python_callable = plot,
    op_kwargs = {'tickers': ['TSLA']},
    provide_context = True,
    dag = dag
)

# Set job dependencies
t0 >> t1
t1 >> t2
t2 >> t3
t3 >> t4
t4 >> t5
