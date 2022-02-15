import pandas as pd

def main():
    excelFile1950s = 'data_files\pe-11-1950s.xls'

    df = pd.read_excel(excelFile1950s)
    print(df)

if __name__ == '__main__':
    main()