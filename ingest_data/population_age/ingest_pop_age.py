import ingest_pop_age_1950_to_1979
import ingest_pop_age_1980_to_1989
import ingest_pop_age_1990_to_1999
import ingest_pop_age_2000_to_2010
import ingest_pop_age_2011_to_2020
import os
import glob
import pandas as pd

# This is the driver module for ingesting all of the U.S. Census Bureau
# population by single year of age data for the years 1950-2020. It
# outputs a normalized CSV file for each distinct data source, then
# combines the data from each file into one CSV file called
# 1950_to_2020_normalized.csv in the normalized_data_files directory.

# The fully-qualified path to the normalized_data_files directory.
# Needs to be changed to wherever this directory lives.
pathToNormalizedDataDirectory = 'my/unique/path'

def combine_csv_files():
    """
    Write the data to a CSV file.

    Returns:
    -----------
    * combinedData: pandas.DataFrame
        The combined data from all CSV files.

    """
    
    # Find all csv files in the directory.
    os.chdir(pathToNormalizedDataDirectory)
    extension = 'csv'
    allFilenames = [i for i in glob.glob('*.{}'.format(extension))]

    # Combine all files in the list.
    combinedData = pd.concat([pd.read_csv(f) for f in allFilenames])

    return combinedData

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
    # Ingest the data from each distinct source.
    ingest_pop_age_1950_to_1979.main()
    ingest_pop_age_1980_to_1989.main()
    ingest_pop_age_1990_to_1999.main()
    ingest_pop_age_2000_to_2010.main()
    ingest_pop_age_2011_to_2020.main()

    # Combine the data into one CSV file.
    combinedData = combine_csv_files()
    write_to_csv(combinedData,
                 '1950_to_2020_normalized.csv')

if __name__ == '__main__':
    main()
