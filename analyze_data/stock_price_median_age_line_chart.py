import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Filepaths to the S&P 500 close price and median age by year
# data files.
stockPriceCsv = 'ingest_data/stock_price/1950_to_2020_s&p500_prices.csv'
medianAgeCsv = 'transform_data/median_age_by_year.csv'

def read_and_join_data(stockPriceCsv, medianAgeCsv):
    """
    Read in the data from the CSV files, join it on Year, and return it
    as a dataframe.
    
    Parameters:
    -----------
    * stockPriceCsv: string
        Filepath to the stock price CSV file.

    * medianAgeCsv: string
        Filepath to the median age CSV file.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The joined data.

    """
    
    # Read the data from the source CSV files.
    stockPriceData = pd.read_csv(stockPriceCsv)
    medianAgeData = pd.read_csv(medianAgeCsv)

    # Join the data on Year.
    joinedData = pd.merge(left=stockPriceData,
                          right=medianAgeData,
                          how='inner',
                          on='Year')

    return joinedData

def plot_data(data):
    """
    Plot the stock price and median age data on a line chart with the 
    same x-axis (Year), each with its own y-axis. Then, save an image of
    the chart. 
    
    Parameters:
    -----------
    * data: pandas.DataFrame
        The stock price and median age data by year.

    """
    
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

    # Plot the age data.
    ax2 = ax.twinx()
    ax2.plot(data['Year'],
             data['Median Age'],
             color='blue',
             marker='o',
             label='Median Age')
    ax2.set_ylabel('Median Age')

    # Modify figure settings.
    fig.legend(loc='upper center')
    fig.set_size_inches(9, 6)

    # Save the chart as a file.
    fig.savefig('analyze_data/stock_price_median_age_line_chart.jpg',
                format='jpeg',
                dpi=100)

def main():
    df = read_and_join_data(stockPriceCsv, medianAgeCsv)
    plot_data(df)

if __name__ == '__main__':
    main()