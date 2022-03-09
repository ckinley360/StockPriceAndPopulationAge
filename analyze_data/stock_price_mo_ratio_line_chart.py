import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Filepaths to the S&P 500 close price and middle-to-old ratio by year
# data files.
stockPriceCsv = 'ingest_data/stock_price/1950_to_2020_s&p500_prices.csv'
moRatioCsv = 'transform_data/middle_to_old_ratio_by_year.csv'

def read_and_join_data(stockPriceCsv, moRatioCsv):
    """
    Read in the data from the CSV files, join it on Year, and return it
    as a dataframe.
    
    Parameters:
    -----------
    * stockPriceCsv: string
        Filepath to the stock price CSV file.

    * moRatioCsv: string
        Filepath to the middle-to-old ratio CSV file.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The joined data.

    """

    # Read the data from the source CSV files.
    stockPriceData = pd.read_csv(stockPriceCsv)
    moRatioData = pd.read_csv(moRatioCsv)

    # Join the data on Year.
    joinedData = pd.merge(left=stockPriceData,
                          right=moRatioData,
                          how='inner',
                          on='Year')

    return joinedData

def plot_data(data):
    """
    Plot the stock price and middle-to-old ratio data on a line chart
    with the same x-axis (Year), each with its own y-axis. Then, save 
    an image of the chart. 
    
    Parameters:
    -----------
    * data: pandas.DataFrame
        The stock price and middle-to-old ratio data by year.

    """

    data['M/O Ratio'] = np.log(data['M/O Ratio'])

    # Create figure and axis objects.
    fig, ax = plt.subplots()

    # Plot the stock data.
    ax.plot(data['Year'],
            data['Close Price'],
            color='red',
            marker='o',
            label='S&P 500 Close Price')
    ax.set_xlabel('Year')
    ax.set_ylabel('S&P 500 Close Price')
    ax.yaxis.set_major_formatter('${x:,.0f}')

    # Plot the m/o ratio data.
    ax2 = ax.twinx()
    ax2.plot(data['Year'],
             data['M/O Ratio'],
             color='blue',
             marker='o',
             label='M/O Ratio')
    ax2.set_ylabel('M/O Ratio')

    # Modify figure settings.
    fig.legend(loc='upper center')
    fig.set_size_inches(9, 6)

    # Save the chart as a file.
    fig.savefig('analyze_data/stock_price_mo_ratio_line_chart.jpg',
                format='jpeg',
                dpi=100)

def main():
    df = read_and_join_data(stockPriceCsv, moRatioCsv)
    plot_data(df)

if __name__ == '__main__':
    main()