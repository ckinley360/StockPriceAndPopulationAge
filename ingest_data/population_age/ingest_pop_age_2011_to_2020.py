import pandas as pd

# This global dataframe will store the cumulative data as it is read in from the different CSV files.
mainDf = pd.DataFrame(columns=['Year', 'Age', 'Population'])

csvFile2011 = 'data_files\\nc-est2019-alldata-p-file04.csv'
csvFile2012 = 'data_files\\nc-est2019-alldata-p-file06.csv'
csvFile2013 = 'data_files\\nc-est2019-alldata-p-file08.csv'
csvFile2014 = 'data_files\\nc-est2019-alldata-p-file10.csv'
csvFile2015 = 'data_files\\nc-est2019-alldata-p-file12.csv'
csvFile2016 = 'data_files\\nc-est2019-alldata-p-file14.csv'
csvFile2017 = 'data_files\\nc-est2019-alldata-p-file16.csv'
csvFile2018 = 'data_files\\nc-est2019-alldata-p-file18.csv'
csvFile2019 = 'data_files\\nc-est2019-alldata-p-file20.csv'
csvFile2020 = 'data_files\\nc-est2019-alldata-p-file22.csv'

def read_and_transform_data(*files):

    """
    Reads in the data from each CSV file, transforms it to fit the target schema, and concatenates the results.

    Parameters:
    -----------
    * *files : string
        Filepaths to CSV files.

    Returns:
    -----------
    * df: pandas dataframe
        The transformed and concatenated data.

    """

    for file in files:
        data = read_csv_file(file)
        transformedData = transform_data(data)
        global mainDf
        mainDf = pd.concat([mainDf, transformedData])
    
    return mainDf

# Read in the CSV file.
def read_csv_file(filePath):
    df = pd.read_csv(filepath_or_buffer=filePath, usecols=['MONTH', 'YEAR', 'AGE', 'TOT_POP'])

    return df
    
# Isolate the data that we are interested in - year, age, and population.
def transform_data(df):
    # Filter out the unneeded rows.
    df = df[(df.MONTH == 7) & (df.AGE != 999)]

    # Now that we've filtered on the MONTH column, we can drop it.
    df = df[['YEAR', 'AGE', 'TOT_POP']]

    # Rename the columns.
    df = df.rename(mapper={'YEAR': 'Year', 'AGE': 'Age', 'TOT_POP': 'Population'}, axis='columns')

    # Convert each dataframe column to integer type.
    df = df.astype({'Year': int, 'Age': int, 'Population': int})

    # Sum the populations of ages 85 and greater, for each year, to put that age range into one bucket - 85. Put the result in a second dataframe.
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
    df.to_csv(path_or_buf=filePath, index=False)
    print(df)

def main():
    data = read_and_transform_data(csvFile2011, csvFile2012, csvFile2013, csvFile2014,
                                   csvFile2015, csvFile2016, csvFile2017, csvFile2018, csvFile2019, csvFile2020)
    write_to_csv(data, 'normalized_data_files/2011_to_2020_normalized.csv')

if __name__ == '__main__':
    main()
