import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Filepaths to the S&P 500 close price and middle age population by year
# data files.
stockPriceCsv = 'ingest_data/stock_price/1950_to_2020_s&p500_prices.csv'
middleAgeCsv = 'transform_data/middle_age_pop_by_year.csv'

def read_and_join_data(stockPriceCsv, middleAgeCsv):
    """
    Read in the data from the CSV files, join it on Year, and return it
    as a dataframe.
    
    Parameters:
    -----------
    * stockPriceCsv: string
        Filepath to the stock price CSV file.

    * middleAgeCsv: string
        Filepath to the middle age population CSV file.
    
    Returns:
    -----------
    * joinedData: pandas.DataFrame
        The joined data.

    """
    
    # Read the data from the source CSV files.
    stockPriceData = pd.read_csv(stockPriceCsv)
    middleAgeData = pd.read_csv(middleAgeCsv)

    # Join the data on Year.
    joinedData = pd.merge(left=stockPriceData,
                          right=middleAgeData,
                          how='inner',
                          on='Year')

    return joinedData

def millions_formatter(x, pos):
    return f'{int(x / 1000000)}'

def plot_data(data):
    """
    Plot the stock price and middle age population data on side-by-side
    line charts. Then, save an image of the chart.
    
    Parameters:
    -----------
    * data: pandas.DataFrame
        The stock price and middle age population data by year.

    """
    
    # Create figure and axis objects.
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(11, 6))

    # Plot the stock data.
    ax[0].plot(data['Year'],
               data['Close Price'],
               color='red',
               marker='o',
               label='Inflation-Adjusted S&P 500 Close Price')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Inflation-Adjusted S&P 500 Close Price')
    ax[0].set_title('Inflation-Adjusted S&P 500 Close Price by Year')
    ax[0].yaxis.set_major_formatter('${x:,.0f}')

    # Plot the middle age data.
    ax[1].plot(data['Year'],
               data['Population'],
               color='blue',
               marker='o',
               label='Middle Age Population')
    ax[1].set_xlabel('Year')
    ax[1].set_ylabel('Middle Age Population (millions)')
    ax[1].set_title('Middle Age Population by Year')
    ax[1].yaxis.set_major_formatter(
        mpl.ticker.FuncFormatter(millions_formatter))

    # Highlight local maxima and minima.
    ax[0].axvspan(1962, 1968, color='black', alpha=0.1)
    ax[1].axvspan(1962, 1968, color='black', alpha=0.1)
    ax[0].axvspan(1978, 1984, color='black', alpha=0.1)
    ax[1].axvspan(1978, 1984, color='black', alpha=0.1)
    ax[0].axvspan(1997, 2003, color='black', alpha=0.1)
    ax[1].axvspan(1997, 2003, color='black', alpha=0.1)

    # Save the chart as a file.
    fig.savefig('analyze_data/stock_price_middle_age_pop_line_chart.jpg',
                format='jpeg',
                dpi=100)

def main():
    df = read_and_join_data(stockPriceCsv, middleAgeCsv)
    plot_data(df)

if __name__ == '__main__':
    main()