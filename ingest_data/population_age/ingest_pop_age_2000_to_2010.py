import pandas as pd

csvFile2000to2010 = 'data_files\\us-est00int-alldata.csv'

# Read in the CSV file.
def readCsvFile(filePath):
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

    return df

def write_to_csv(df, filePath):
    df.to_csv(path_or_buf=filePath, index=False)

def main():
    df = readCsvFile(csvFile2000to2010)
    transformedDf = transform_data(df)
    write_to_csv(transformedDf, 'normalized_data_files/2000_to_2010_normalized.csv')

if __name__ == '__main__':
    main()
