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

def compute_middle_to_old_ratio(df):
    """
    Compute the middle-to-old ratio by year. Middle age is defined as
    ages 40-49. Old age is defined as ages 60-69.
    
    Parameters:
    -----------
    * df: pandas.DataFrame
        The data to compute middle-to-old ratio by year for.
        
    Returns:
    -----------
    * df: pandas.DataFrame
        Middle-to-old ratio by year.

    """

    # Label the Middle and Old age ranges, and filter out the rest.
    conditions = [(df['Age'] >= 40) & (df['Age'] <= 49),
                  (df['Age'] >= 60) & (df['Age'] <= 69)]
    choices = ['Middle', 'Old']
    df['Age Category'] = np.select(conditions, choices, default='Other')
    df = df[df['Age Category'] != 'Other']

    # Sum the population for Middle and Old by year.
    df = df.drop('Age', axis=1) # Drop Age column since we no longer need it.
    df = df.groupby(['Year', 'Age Category'], as_index=False).sum(['Population'])
    df = df.pivot(index='Year', columns='Age Category', values='Population')

    # Compute the middle-to-old ratio by year.
    df['M/O Ratio'] = df['Middle'] / df['Old']

    # Drop the Middle and Old columns since we no longer need them.
    df = df.drop(['Middle', 'Old'], axis=1)

    # Round the ratio to 3 decimal places.
    df['M/O Ratio'] = df['M/O Ratio'].round(3)

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

    df.to_csv(path_or_buf=filePath, index=True)

def main():
    data = read_csv_file(population1950to2020)
    middleToOldRatioByYear = compute_middle_to_old_ratio(data)
    write_to_csv(middleToOldRatioByYear,
                 'transform_data/middle_to_old_ratio_by_year.csv')

if __name__ == '__main__':
    main()