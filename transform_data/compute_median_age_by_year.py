import pandas as pd
import numpy as np

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

def compute_median_age_by_year(df):
    df = df[df.Year == 1950]

    # Compute the median age by year.
    df = df.groupby(['Year']).apply(lambda x: compute_median_age(x)).to_frame('Median Age')

    return df

def compute_median_age(df):
    median = (np.repeat(df['Age'], df['Population'])).median()

    return median

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

    df.to_csv(path_or_buf=filePath)

def main():
    data = read_csv_file(population1950to2020)
    medianAgeByYear = compute_median_age_by_year(data)
    print(medianAgeByYear)
    write_to_csv(medianAgeByYear,
                'transform_data/median_age_by_year.csv')

if __name__ == '__main__':
    main()