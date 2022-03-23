import pandas as pd
from scipy.stats import linregress
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

def compute_simple_linear_regression_equation(independentVariable, dependentVariable):
    """
    Compute a simple linear regression equation for the input variables.
    
    Parameters:
    -----------
    * independentVariable: array_like
        The independent variable.

    * dependentVariable: array_like
        The dependent variable.

    Returns:
    -----------
    * result: scipy.stats.LinregressResult
        A linear regression result object.

    """

    result = linregress(independentVariable, dependentVariable)

    return result

def millions_formatter(x, pos):
    """
    Format the input number as millions (rather than raw value).
    
    Parameters:
    -----------
    * x: int
        The tick value (number) to format.

    * pos: int
        The position (not used, but still required in function
        definition).

    Returns:
    -----------
    * formattedTickLabel: string
        The formatted tick label.

    """

    formattedTickLabel = str(int(x / 1000000))

    return formattedTickLabel

def plot_regression_line(x, y, linearRegressionResult):
    plt.plot(x, y, 'o', label='Actual Data')
    plt.plot(x, 
             linearRegressionResult.slope*x + 
             linearRegressionResult.intercept,
             'r',
             label='Fitted Line (y = ' + 
             str(linearRegressionResult.slope) + 'x + ' + 
             str(linearRegressionResult.intercept) + ')')
    plt.legend()

    fig = plt.gcf()
    ax = fig.gca()
    
    fig.set_size_inches(11, 6)
    ax.set_title(
        'Middle Age Population and Inflation-Adjusted S&P 500 Close Price Scatter Plot')
    ax.set_ylabel('Inflation-Adjusted S&P 500 Close Price')
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.set_xlabel('Middle Age Population (millions)')
    ax.xaxis.set_major_formatter(
        mpl.ticker.FuncFormatter(millions_formatter))

    plt.show()

def main():
    df = read_and_join_data(stockPriceCsv, middleAgeCsv)
    linearRegressionResult = compute_simple_linear_regression_equation(
        df['Population'],
        df['Close Price'])
    plot_regression_line(df['Population'],
                         df['Close Price'],
                         linearRegressionResult)


if __name__ == '__main__':
    main()
