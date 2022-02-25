import pandas as pd
import requests

# The API URL path and parameters for the GET request to the Population 
# Estimates REST API. API documentation located here: 
# https://www.census.gov/data/developers/data-sets/popest-popproj/popest.1990-2000_Intercensals.html
url = 'https://api.census.gov/data/1990/pep/int_natresafo'
parameters = {
    'get': 'YEAR,AGE,TOT_POP',
    'key': 'my key'
}

def get_data(url, parameters):
    """
    Issue a GET request to the REST API to get the data we are 
    interested in - population by single year of age for the years 
    1990-1999.

    Parameters:
    -----------
    * url : string
        The API URL path.

    * parameters : dictionary
        The GET request parameters.

    Returns:
    -----------
    * responseString : string
        A string representation of the server's response.

    """
    
    response = requests.get(url=url, params=parameters)
    responseString = response.text
    
    return responseString

def transform_data(data):
    """
    Transform the data to fit the target schema, and return the data as 
    a dataframe.

    Parameters:
    -----------
    * data : string
        The data to transform.

    Returns:
    -----------
    * df : pandas.DataFrame
        The transformed data.

    """
    
    # Remove double quotes, left square bracket, and right 
    # square bracket.
    data = data.replace('"', '').replace('[', '').replace(']', '')

    # Split the string on comma + newline to create a list of strings.
    data = data.split(',\n')

    # Split each string in the list on comma to create a 
    # two-dimensional list.
    index = 0
    for string in data:
        data[index] = string.split(',')
        index += 1

    # Convert the two-dimensional list into a dataframe.
    df = pd.DataFrame(data=data, columns=['Year', 'Age', 'Population'])

    # Filter out the old header row, total population rows (age 999), 
    # and populations for the year 2000.
    df = df[(df.Year != 'YEAR') & 
            (df.Age != '999') & 
            (df.Year != '2000')]

    # Convert each dataframe column to integer type.
    df = df.astype({'Year': int, 'Age': int, 'Population': int})

    # Sum the populations of ages 85 and greater, for each year, to put 
    # that age range into one bucket - 85. Put the result in a 
    # second dataframe.
    dfEightyFiveBucket = df[df.Age >= 85]
    dfEightyFiveBucket = dfEightyFiveBucket.groupby(['Year']).sum()
    dfEightyFiveBucket['Age'] = 85
    dfEightyFiveBucket = dfEightyFiveBucket.reset_index()

    # Filter out ages 85 and greater from the first dataframe.
    df = df[df.Age < 85]

    # Concatenate the second dataframe with the first dataframe.
    df = pd.concat([df, dfEightyFiveBucket])

    return df
    
def write_to_csv(df, filePath):
    """
    Write the data to a CSV file.

    Parameters:
    -----------
    * df : pandas.DataFrame
        The data to write.

    * filePath : string
        The filepath to write the data to.

    """

    df.to_csv(path_or_buf=filePath, index=False)

def main():
    data = get_data(url, parameters)
    transformedData = transform_data(data)
    write_to_csv(transformedData, 
                 'normalized_data_files/1990_to_1999_normalized.csv')

if __name__ == '__main__':
    main()
