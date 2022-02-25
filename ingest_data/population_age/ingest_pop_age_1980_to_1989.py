import csv

# Filepaths to the fixed-width text files containing population by 
# single year of age for the years 1980-1989. Sourced from "Quarterly 
# Intercensal Estimates of Resident Population plus Armed Forces 
# overseas" section of
# https://www.census.gov/data/datasets/time-series/demo/popest/1980s-national.html
textFile1980to1981 = 'data_files\E8081PQI.TXT'
textFile1981to1982 = 'data_files\E8182PQI.TXT'
textFile1982to1983 = 'data_files\E8283PQI.TXT'
textFile1983to1984 = 'data_files\E8384PQI.TXT'
textFile1984to1985 = 'data_files\E8485PQI.TXT'
textFile1985to1986 = 'data_files\E8586PQI.TXT'
textFile1986to1987 = 'data_files\E8687PQI.TXT'
textFile1987to1988 = 'data_files\E8788PQI.TXT'
textFile1988to1989 = 'data_files\E8889PQI.TXT'
textFile1989to1990 = 'data_files\E8990PQI.TXT'

def read_and_transform_data(*filePaths):
    """
    Read in the data from each text file, transform it to fit the target
    schema, and concatenate the results into one list.
    
    Parameters:
    -----------
    * *filePaths : string
        Filepaths to text files.
    
    Returns:
    -----------
    * list : list
        The transformed and concatenated data.
    
    """

    # Stores the cumulative data as it is read in from the different 
    # text files and transformed.
    list = []

    for filePath in filePaths:
        file = read_text_file(filePath)
        transformedData = transform_data(file)
        list.extend(transformedData)

    return list

def read_text_file(filePath):
    """
    Open the file to read.

    Parameters:
    -----------
    * filePath : string
        Filepath to the text file.

    Returns:
    -----------
    * file : file
        The text file.

    """
    
    file = open(filePath, 'r')

    return file

def transform_data(file):
    """
    Transform the data in the file to fit the target schema, and return 
    the data as a list.
    
    Parameters:
    -----------
    * file : file
        The file containing the data to transform.
    
    Returns:
    -----------
    * list : list
        The transformed data.
    
    """

    # Stores the cumulative data as each line of the file is read and 
    # transformed.
    list = []

    # Any age greater than or equal to 85 will be lumped into one 
    # bucket - 85. This will track the sum of age 85 or greater for 
    # each year.
    populationAge85OrGreater = 0

    # Read all lines of the file.
    while True:
        line = file.readline()

        # If end of file is reached, then stop reading lines.
        if line == '\x1a\n':
            break

        # Extract the data we are interested in - year, age, and total 
        # population. We only want the July (month 7) population 
        # estimate for each year, so we will extract month as well so we
        # can filter on it.
        month = int(line[2:4].strip())
        year = int('19' + line[4:6].strip())
        age = int(line[6:9].strip())
        population = int(line[10:20].strip())

        # Filter to get July's estimate by single year of age.
        if (month == 7 and age != 999):
            # If the age is greater than or equal to 85, then add the 
            # population to our populationAge85OrGreater tracker.
            if age >= 85:
                populationAge85OrGreater += population

                # We want to sum age 85 through 100 before appending the
                # list to mainList. If the age is less than 100, then 
                # read in the next line without appending the list 
                # to mainList.
                if age < 100:
                    continue

            # If age is 100, then append the summed population to the 
            # main list and reset the populationAge85OrGreater tracker 
            # to zero.
            if age == 100:
                list.append([year, 85, populationAge85OrGreater])
                populationAge85OrGreater = 0
            # Otherwise, append this list (representing the population 
            # of a specific age group for a given year) to the main list.
            else:
                list.append([year, age, population])

    # Close the file.
    file.close()

    return list

def write_to_csv(list, filePath):
    """
    Write the data to a CSV file.
    
    Parameters:
    -----------
    * list : list
        The data to write.
    
    * filePath : string
        The filepath to write the data to.
    
    """
    
    with open(file=filePath, mode='w', newline='') as file:
        rowWriter = csv.writer(file)
        header = ['Year', 'Age', 'Population']
        rowWriter.writerow(header)
        
        for row in list:
            rowWriter.writerow(row)

def main():
    data = read_and_transform_data(textFile1980to1981, textFile1981to1982, 
                                   textFile1982to1983, textFile1983to1984, 
                                   textFile1984to1985, textFile1985to1986, 
                                   textFile1986to1987, textFile1987to1988, 
                                   textFile1988to1989, textFile1989to1990)
    write_to_csv(data, 'normalized_data_files/1980_to_1989_normalized.csv')

if __name__ == '__main__':
    main()
