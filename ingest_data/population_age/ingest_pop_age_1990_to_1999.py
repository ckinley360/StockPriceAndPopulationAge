import requests
import pandas as pd

url = 'https://api.census.gov/data/1990/pep/int_natresafo'
parameters = {
    'get': 'YEAR,AGE,TOT_POP',
    'key': 'my key'
}

# Issue a GET request to the API to get the data we are interested in - year, age, and population.
# The response is a two-dimensional list containing the columns YEAR, AGE, and TOT_POP.
def getData(url, parameters):
    response = requests.get(url=url, params=parameters)
    return response.text

def parseData(data):
    df = pd.DataFrame(data=data, index=None, columns=['YEAR', 'AGE', 'TOT_POP'])
    print(df)

def write_to_csv(list, filePath):
    print('hello')

def main():
    data = getData(url, parameters)
    parseData(data)

if __name__ == '__main__':
    main()
