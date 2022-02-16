import pandas as pd

# This global dataframe will store the cumulative data as it is read in from the different Excel files and tabs
mainDf = pd.DataFrame(columns=['Year', 'Age', 'Population'])

excelFile1950s = 'data_files\pe-11-1950s.xls'
excelFile1960s = 'data_files\pe-11-1960s.xls'
excelFile1970s = 'data_files\pe-11-1970s.xls'

def read_excel_file(filePath):
    # Read in the Excel file, and isolate the data we are interested in - total pouplation of all races by single year of age
    df = pd.read_excel(io=filePath, header=5, names=['Age','Population'], usecols=[0,1])
    df = df[(df.Population.notnull()) & (df.Age != 'All ages')]
    df = df.astype({'Population':int})
    df = df.replace(to_replace='85+', value='85')

    # Add a column that contains the year of the population estimate, then rearrange the columns
    df['Year'] = 1950
    df = df[['Year', 'Age', 'Population']]
    
    # Concatenate this dataframe with the global dataframe
    global mainDf
    mainDf = pd.concat([mainDf, df])

def main():
    read_excel_file(excelFile1950s)
    print(mainDf)

if __name__ == '__main__':
    main()
