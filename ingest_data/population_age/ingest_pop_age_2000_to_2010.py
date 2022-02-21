import pandas as pd

csvFile2000to2010 = 'data_files\\us-est00int-alldata.csv'

# Read in the Excel file, and isolate the data we are interested in - year, age, and population.
def readCsvFile(filePath):
    df = pd.read_csv(filepath_or_buffer=filePath, usecols=['YEAR', 'AGE', 'TOT_POP'])

    # Rename the columns.
    df = df.rename({'YEAR': 'Year', 'AGE': 'Age', 'TOT_POP': 'Population'})

    # Filter out the unneeded columns and rows.
    df = df[(df.Month == 7) & (df.Age != 999)]

    return df
    
def write_to_csv(df, filePath):
    df.to_csv(path_or_buf=filePath, index=False)

def main():
    df = readCsvFile(csvFile2000to2010)
    print(df)

if __name__ == '__main__':
    main()