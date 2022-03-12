import pandas as pd
import numpy as np

# Filepath to the normalized population by single year of age data for
# the years 1950-2020.
population1950to2020 = 'ingest_data/population_age/normalized_data_files/1950_to_2020_normalized.csv'

def read_csv_file(filePath):
    """
    Read in the data from the CSV file and return the data as a 
    dataframe.
    
    Parameters:
    -----------
    * filePath: string
        Filepath to the CSV file.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The data.

    """

    df = pd.read_csv(filepath_or_buffer=filePath)

    return df

def compute_middle_age_pop(df):
    """
    Compute the middle age population by year. Middle age is defined as
    ages 40-49.
    
    Parameters:
    -----------
    * df: pandas.DataFrame
        The data to compute middle age population by year for.
        
    Returns:
    -----------
    * df: pandas.DataFrame
        Middle age population by year.

    """

    # Filter out non-middle age populations.
    df = df[(df['Age'] >= 40) & (df['Age'] <= 49)]

    # Sum the population for middle age by year.
    df = df.drop('Age', axis=1) # Drop Age column since we no longer need it.
    df = df.groupby(['Year'], as_index=False).sum(['Population'])

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
    data = read_csv_file(population1950to2020)
    middleAgePopByYear = compute_middle_age_pop(data)
    write_to_csv(middleAgePopByYear,
                 'transform_data/middle_age_pop_by_year.csv')

if __name__ == '__main__':
    main()