import requests
import pandas as pd

url = 'https://api.census.gov/data/1990/pep/int_natresafo'
parameters = {
    'get': 'YEAR,AGE,TOT_POP',
    'key': 'my key'
}

# Issue a GET request to the API to get the data we are interested in - year, age, and population.
# Return a string representation of the response.
def getData(url, parameters):
    response = requests.get(url=url, params=parameters)
    return response.text

def parseData(data):
    # Remove double quotes, left square bracket, and right square bracket.
    data = data.replace('"', '').replace('[', '').replace(']', '')

    # Split the string on comma + newline to create a list of strings.
    data = data.split(',\n')

    # Split each string in the list on comma to create a two-dimensional list.
    index = 0
    for string in data:
        data[index] = string.split(',')
        index += 1

    # Convert the two-dimensional list into a dataframe.
    df = pd.DataFrame(data=data, columns=['Year', 'Age', 'Population'])

    # Filter out the old header row, total population rows (age 999), and populations for the year 2000.
    df = df[(df.Year != 'YEAR') & (df.Age != '999') & (df.Year != '2000')]

    # Convert each dataframe column to integer type.
    df = df.astype({'Year': int, 'Age': int, 'Population': int})

    # Sum the populations of ages 85 and greater to put it into one bucket - 85.
    

    print(df)
    
def write_to_csv(list, filePath):
    print('hello')

def main():
    data = getData(url, parameters)
    parseData(data)

if __name__ == '__main__':
    main()
