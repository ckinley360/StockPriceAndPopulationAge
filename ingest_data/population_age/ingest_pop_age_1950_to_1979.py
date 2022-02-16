import pandas as pd

def main():
    excelFile1950s = 'data_files\pe-11-1950s.xls'

    df = pd.read_excel(io=excelFile1950s, header=5, names=['Age','Population'], usecols=[0,1])
    df = df[(df.Population.notnull()) & (df.Age != 'All ages')]
    df = df.astype({'Population':int})
    df = df.replace(to_replace='85+', value='85')
    print(df)

if __name__ == '__main__':
    main()
