import csv

# This global list will store the cumulative data as it is read in from the text files.
mainList = []

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

# Read in the text files.
def read_text_files(*files):
    for file in files:
        read_text_file(file)

# Read in the text file, and isolate the data we are interested in - year, age, and population.
def read_text_file(filePath):
    # We are going to append the population of each age group for each year (represented as a list) to the main list.
    global mainList
    
    # Open the file and start reading it.
    with open(filePath, 'r') as file:
        # Any age greater than or equal to 85 will be lumped into one bucket - 85.
        # This will track the sum of age 85 or greater for each year.
        populationAge85OrGreater = 0

        # Read all lines of the file.
        while True:
            line = file.readline()

            # If end of file is reached, then stop reading lines.
            if line == '\x1a\n':
                break
            
            # Extract the data we are interested in - year, age, and total population.
            # We only want the July (month 7) population estimate for each year, so we will extract month as well so we can filter on it.
            month = int(line[2:4].strip())
            year = int('19' + line[4:6].strip())
            age = int(line[6:9].strip())
            population = int(line[10:20].strip())

            # Filter to get July's estimate by single year of age.
            if (month == 7 and age != 999):
                # If the age is greater than or equal to 85, then add the population to our populationAge85OrGreater tracker.
                if age >= 85:
                    populationAge85OrGreater += population

                    # We want to sum age 85 through 100 before appending the list to mainList.
                    # If the age is less than 100, then read in the next line without appending the list to mainList.
                    if age < 100:
                        continue
                
                # If age is 100, then append the summed population to mainList and reset the populationAge85OrGreater tracker to zero.
                if age == 100:
                    mainList.append([year, 85, populationAge85OrGreater])
                    populationAge85OrGreater = 0
                # Otherwise, append this list (representing the population of a specific age group for a given year) to mainList.
                else:
                    mainList.append([year, age, population])

def write_to_csv(list, filePath):
    with open(file=filePath, mode='w', newline='') as file:
        rowWriter = csv.writer(file)
        header = ['Year', 'Age', 'Population']
        rowWriter.writerow(header)
        
        for row in list:
            rowWriter.writerow(row)

def main():
    read_text_files(textFile1980to1981, textFile1981to1982, textFile1982to1983, textFile1983to1984, textFile1984to1985,
                    textFile1985to1986, textFile1986to1987, textFile1987to1988, textFile1988to1989, textFile1989to1990)
    write_to_csv(mainList, 'normalized_data_files/1980_to_1989_normalized.csv')

if __name__ == '__main__':
    main()
