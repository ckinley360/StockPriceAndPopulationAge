import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.multpl.com/inflation-adjusted-s-p-500/table/by-year'

def scrape_webpage(url):
    page = requests.get(url)

    return page

def parse_data(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    dataTable = soup.find(id='datatable')
    rows = dataTable.find_all('tr')
    
    df = pd.DataFrame(columns=('Year', 'Close Price'))
    for row in rows[1:]:
        columnOneValue = row.find('td', class_='left').text
        columnTwoValue = row.find('td', class_='right').text
        print(columnOneValue + ', ' + columnTwoValue)

def main():
    page = scrape_webpage(url)
    parse_data(page)

if __name__ == '__main__':
    main()