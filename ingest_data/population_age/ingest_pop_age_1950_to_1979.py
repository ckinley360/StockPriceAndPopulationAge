import pandas as pd

# Filepaths to the Excel files containing population by single year of age for the years 1950-1979.
# Sourced from "Population by age, sex, and race" section of
# https://www.census.gov/data/tables/time-series/demo/popest/pre-1980-national.html
excelFile1950s = 'data_files\pe-11-1950s.xls'
excelFile1960s = 'data_files\pe-11-1960s.xls'
excelFile1970s = 'data_files\pe-11-1970s.xls'

def read_and_transform_data(*files):
    """
    Read in the data from each Excel file, transform it to fit the target schema, and concatenate the results into one dataframe.
    
    Parameters:
    -----------
    * *files : string
        Filepaths to Excel files.
    
    Returns:
    -----------
    * df: pandas.DataFrame
        The transformed and concatenated data.
    
    """

    # Stores the cumulative data as it is read in from the different Excel files and transformed.
    df = pd.DataFrame(columns=['Year', 'Age', 'Population'])

    for file in files:
        data = read_excel_file(file)
        transformedData = transform_data(data)
        df = pd.concat([df, transformedData])

    return df

def read_excel_file(filePath):
    """
    Read in the data from each Excel file, isolate the columns of interest, and return the data as a dictionary.
    
    Parameters:
    -----------
    * filePath : string
        Filepath to the Excel file.
    
    Returns:
    -----------
    * sheetsDict : dictionary
        The data for the columns of interest.
        Key = sheet name
        Value = sheet data
    
    """
    
    sheetsDict = pd.read_excel(io=filePath, sheet_name=None, header=5, names=['Age','Population'], usecols=[0,1])

    return sheetsDict

def transform_data(sheetsDict):
    """
    Transform the data to fit the target schema, and return the data as a dataframe.
    
    Parameters:
    -----------
    * sheetsDict : dictionary
        The data to transform.
    
    Returns:
    -----------
    * sheetDf: pandas.DataFrame
        The transformed data.
    
    """

    # Extract the data from each sheet, filter out unneeded rows, and normalize.
    for sheetName, sheetDf in sheetsDict.items():
        sheetDf = sheetDf[(sheetDf.Population.notnull()) & (sheetDf.Age != 'All ages')]
        sheetDf = sheetDf.astype({'Population': int})
        sheetDf = sheetDf.replace(to_replace='85+', value='85')

        # Add a column that contains the year of the population estimate, then rearrange the columns.
        sheetDf['Year'] = sheetName
        sheetDf = sheetDf[['Year', 'Age', 'Population']]

        return sheetDf

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
    data = read_and_transform_data(excelFile1950s, excelFile1960s, excelFile1970s)
    write_to_csv(data, 'normalized_data_files/1950_to_1979_normalized.csv')

if __name__ == '__main__':
    main()
