# This global list will store the cumulative data as it is read in from the different text files.
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

def read_text_file(filePath):
    # Open the file and start reading it.
    with open(filePath, 'r') as file:
        while True:
            line = file.readline()

            # If end of file is reached, then stop reading lines.
            if line == '\x1a\n':
                break
            
            # Extract the data we are interested in - year, age, and total population.
            month = int(line[2:4].strip())
            year = int('19' + line[4:6].strip())
            age = int(line[6:9].strip())
            population = int(line[10:20].strip())

            # We only want July's estimate by single year of age. If this row meets these criteria, then create a list of the data and append it to the global list.
            if (month == 7 and age != 999):
                # Any age greater than or equal to 85 will be lumped into one bucket - 85.
                if age >= 85:
                    
                global mainList
                mainList.append([year, age, population])
                

def main():
    read_text_file(textFile1980to1981)
    for list in mainList:
        print(list)

if __name__ == '__main__':
    main()
