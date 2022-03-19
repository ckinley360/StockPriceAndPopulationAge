import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

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
    * df: pandas.DataFrame
        The joined data.

    """

    # Read the data from the source CSV files.
    stockPriceData = pd.read_csv(stockPriceCsv)
    middleAgeData = pd.read_csv(middleAgeCsv)

    # Join the data on Year.
    preparedData = pd.merge(left=stockPriceData,
                            right=middleAgeData,
                            how='inner',
                            on='Year')

    return preparedData

def millions_formatter(x, pos):
    return f'{int(x / 1000000)}'

def plot_data(data):
    """
    Plot the stock price and middle age population data on a scatter
    plot. Then, save an image of the plot.
    
    Parameters:
    -----------
    * data: pandas.DataFrame
        The stock price and middle age population data by year.

    """

    # Create figure and axis objects.
    pathCollection = plt.scatter(data['Population'], data['Close Price'])
    pathCollection.get_figure().set_size_inches((11, 6))

    pathCollection.axes.set_title(
        'Middle Age Population and Inflation-Adjusted S&P 500 Close Price Scatter Plot')
    pathCollection.axes.set_ylabel('Inflation-Adjusted S&P 500 Close Price')
    pathCollection.axes.yaxis.set_major_formatter('${x:,.0f}')
    pathCollection.axes.set_xlabel('Middle Age Population (millions)')
    pathCollection.axes.xaxis.set_major_formatter(
        mpl.ticker.FuncFormatter(millions_formatter))

    # Save the chart as a file.
    pathCollection.get_figure().savefig(
        'analyze_data/stock_price_middle_age_pop_scatter_plot.jpg',
        format='jpeg',
        dpi=100)

def compute_pearson_correlation_coefficient(data):
    p, _ = pearsonr(data['Population'], data['Close Price'])
    p = round(p, 2)

    return p

def main():
    df = read_and_join_data(stockPriceCsv, middleAgeCsv)
    plot_data(df)
    p = compute_pearson_correlation_coefficient(df)
    print('Pearson\'s population correlation coefficient: ' + str(p))

if __name__ == '__main__':
    main()