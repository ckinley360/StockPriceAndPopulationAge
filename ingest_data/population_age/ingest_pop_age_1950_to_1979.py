import pandas as pd

# This global dataframe will store the cumulative data as it is read in from the different Excel files and tabs
mainDf = pd.DataFrame(columns=['Year', 'Age', 'Population'])

excelFile1950s = 'data_files\pe-11-1950s.xls'
excelFile1960s = 'data_files\pe-11-1960s.xls'
excelFile1970s = 'data_files\pe-11-1970s.xls'

# Read in the Excel files.
def read_excel_files(*files):
    for file in files:
        read_excel_file(file)

# Read in the Excel file, and isolate the data we are interested in - total pouplation of all races by single year of age.
def read_excel_file(filePath):
    sheets_dict = pd.read_excel(io=filePath, sheet_name=None, header=5, names=['Age','Population'], usecols=[0,1])

    # Loop through the dictionary and extract the data from each sheet.
    for sheet_name, sheet_df in sheets_dict.items():
        sheet_df = sheet_df[(sheet_df.Population.notnull()) & (sheet_df.Age != 'All ages')]
        sheet_df = sheet_df.astype({'Population':int})
        sheet_df = sheet_df.replace(to_replace='85+', value='85')

        # Add a column that contains the year of the population estimate, then rearrange the columns.
        sheet_df['Year'] = sheet_name
        sheet_df = sheet_df[['Year', 'Age', 'Population']]
        
        # Concatenate this dataframe with the global dataframe.
        global mainDf
        mainDf = pd.concat([mainDf, sheet_df])

# Write the data in the dataframe to a csv file with name fileName.
def write_to_csv(df, fileName):
    df.to_csv(path_or_buf='normalized_data_files/'+fileName+'.csv', index=False)

def main():
    read_excel_files(excelFile1950s, excelFile1960s, excelFile1970s)
    write_to_csv(mainDf, '1950_to_1979_normalized')

if __name__ == '__main__':
    main()
