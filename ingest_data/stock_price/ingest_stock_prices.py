import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.multpl.com/inflation-adjusted-s-p-500/table/by-year'

def scrape_webpage(url):
    """
    Scrape the webpage containing historical S&P 500 close price data
    and return the response object.

    Parameters:
    -----------
    * url: string
        The URL of the desired webpage.
    
    Returns:
    -----------
    * page: requests.Response
        The response object containing the data of the desired webpage.

    """

    page = requests.get(url)

    return page

def parse_data(page):
    """
    Extract the year and closing price data from the data table of the
    page, and return it as a dataframe.

    Parameters:
    -----------
    * page: requests.Response
        The response object containing the data of the desired webpage.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The year and closing price data for the years 1950-2020.

    """
    
    # Isolate the rows of the data table.
    soup = BeautifulSoup(page.content, 'html.parser')
    dataTable = soup.find(id='datatable')
    rows = dataTable.find_all('tr')
    
    # Create the dataframe and initialize the index tracker.
    df = pd.DataFrame(columns=('Year', 'Close Price'))
    index = 0

    # Extract the year and closing price from each row, and store them
    # in the dataframe.
    for row in rows[1:]:
        columnOneValue = row.find('td', class_='left').text
        columnTwoValue = row.find('td', class_='right').text
        year = int((columnOneValue.split(','))[1].strip())
        price = float(columnTwoValue.replace(',', '').strip())
        df.loc[index] = [year, price]
        index += 1

    # Change the column types and filter for the desired years.
    df = df.astype({'Year': int,
                    'Close Price': float})
    df = df[(df.Year >= 1950) & (df.Year <= 2020)]

    return df

def write_to_csv(df, filePath):
    """
    Write the data to a CSV file.
    
    Parameters:
    -----------
    * df: pandas.DataFrame
        The data to write.
    
    * filePath: string
        The filepath to write the data to.
    
    """

    df.to_csv(path_or_buf=filePath, index=False)

def main():
    page = scrape_webpage(url)
    data = parse_data(page)
    write_to_csv(data, 'ingest_data/stock_price/1950_to_2020_s&p500_prices.csv')

if __name__ == '__main__':
    main()