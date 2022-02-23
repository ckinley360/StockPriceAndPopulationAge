import pandas as pd

# Filepath to the CSV file containing population by single year of age for the years 2000-2010.
# Sourced from "Intercensal Estimates of the Resident Population by Single Year of Age, Sex, Race, and Hispanic Origin for the United States: April 1, 2000 to July 1, 2010" section of
# https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-national.html
csvFile2000to2010 = 'data_files\\us-est00int-alldata.csv'

def read_csv_file(filePath):
    """
    Read in the data from the CSV file, isolate the columns of interest, and return the data as a dataframe.
    
    Parameters:
    -----------
    * filePath : string
        Filepath to the CSV file.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The data for the columns of interest.

    """
    
    df = pd.read_csv(filepath_or_buffer=filePath, usecols=['MONTH', 'YEAR', 'AGE', 'TOT_POP'])

    return df

def transform_data(df):
    """
    Transform the data to fit the target schema, and return the data as a dataframe.
    
    Parameters:
    -----------
    * df : pandas.DataFrame
        The data to transform.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The transformed data.

    """

    # Filter out the unneeded rows.
    df = df[(df.MONTH == 7) & (df.AGE != 999)]

    # Now that we've filtered on the MONTH column, we can drop it.
    df = df[['YEAR', 'AGE', 'TOT_POP']]

    # Rename the columns.
    df = df.rename(mapper={'YEAR': 'Year', 'AGE': 'Age', 'TOT_POP': 'Population'}, axis='columns')

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
    df = read_csv_file(csvFile2000to2010)
    transformedDf = transform_data(df)
    write_to_csv(transformedDf, 'normalized_data_files/2000_to_2010_normalized.csv')

if __name__ == '__main__':
    main()
