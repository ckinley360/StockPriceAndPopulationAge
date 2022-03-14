# Stock Price And Population Age
A high-level analysis of the relationship between U.S. stock prices and U.S. age demographics.

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Data Ingestion](#data-ingestion)

## General Information
According to [Investopedia](https://www.investopedia.com/articles/basics/04/100804.asp#:~:text=traders%20and%20investors.-,Fundamental%20Factors,as%20a%20P%2FE%20ratio), there are three categories of forces that affect stock prices - fundamental factors, technical factors, and market sentiment. Of these three forces, I find technical factors to be the most interesting, specifically age demographics. With [reports](https://www.bbc.com/news/world-us-canada-57003722) of the U.S. birth rate declining (along with many other countries), I was curious what impact, if any, it might have on the stock market. To explore the potential relationship between stock prices and age demographics, I compared historical inflation-adjusted close prices of the S&P 500 with U.S. population age data for the years 1950-2020.

The S&P 500 index is widely seen as representative of the health of the U.S. economy, and since I'm interested in analyzing stock prices at a macro-level, it seemed like a great choice. I used inflation-adjusted close prices to eliminate inflation as a factor for the change in close prices so that I could have an "apples-to-apples" comparison over time. [multpl](https://www.multpl.com/inflation-adjusted-s-p-500/table/by-year) has a nice table of historical inflation-adjusted S&P 500 close prices, and this is the source of the stock price data that I used.

The [U.S. Census Bureau](https://www.census.gov/data.html) has a treasure trove of publicly available demographic data, including the estimated population of the U.S. over time, broken down by single year of age. This is the source of the age data that I used.

## Technologies Used
- Python 3.10.2

## Setup
Project dependencies are listed in the /requirements.txt file.

## Data Ingestion
### Population Age Data
#### Disclaimer

This product uses the Census Bureau Data API but is not endorsed or certified by the Census Bureau.

#### Data Source

All population age data is sourced from the [United States Census Bureau website](https://www.census.gov/data.html). To get the entire population of the United States, I used the Estimated Resident Population plus Armed Forces Overseas. To be able to calculate the median age for each year, I used the population estimates that are broken down by Single Year of Age. Data for different years is structured differently, and so I wrote custom Python scripts to ingest each unique data source.

- **1950 - 1979:** [Excel files](https://www.census.gov/data/tables/time-series/demo/popest/pre-1980-national.html). Annual estimate calculated in July.
- **1980 - 1989:** [Fixed-width text files](https://www.census.gov/data/datasets/time-series/demo/popest/1980s-national.html) decoded with file layout specification (modified for 2-digit year for pre-1990 estimates that use this file structure). I used the July estimate for each year.
- **1990 - 1999:** [Population Estimates API](https://www.census.gov/data/developers/data-sets/popest-popproj/popest.1990-2000_Intercensals.html). Annual estimate calculated in April.
- **2000 - 2010:** [CSV file](https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-national.html). I used the July estimate for each year.
- **2011 - 2020:** [CSV files](https://www.census.gov/data/tables/time-series/demo/popest/2010s-national-detail.html). I used the July estimate for each year.

To verify that I pulled the data correctly, I used the [Federal Reserve Bank of St. Louis's population data](https://fred.stlouisfed.org/graph/?id=POP,) as a cross-check. There are some small differences due to the St. Louis Fed's rounding, and potentially pulling data from a United States Census Bureau source that was calculated in a slightly different way (you can get population estimates for the same date range in multiple places on the Census Bureau's website).

#### Data Normalization

Since each unique data source is structured differently, I normalized the population data to conform to this schema:

| Year (int) | Age (int) | Population (int) |
| ---------- | --------- | ---------------- |
| 1950       | 0         | 3,162,567        |
| 1950       | 1         | 3,299,863        |
| ...        | ...       | ...              |
| 1950       | 85        | 589,612          |
| 1951       | 0         | 3,315,027        |
| ...        | ...       | ...              |
| 2020       | 85        |  6,739,054       |

Due to some data sources lumping all ages greater than 84 into one bucket - 85+ - the age 85 in my schema represents 85+. 

#### Driver Module
The driver module for ingesting the population age data is **ingest_pop_age.py**.

### Stock Price Data
The historical inflation-adjusted S&P 500 close prices were scraped from the table on [multpl](https://www.multpl.com/inflation-adjusted-s-p-500/table/by-year). The data was filtered to the years 1950-2020, the year portion of the date was extracted, and the resulting data was written to a CSV file.

<img src="analyze_data/stock_price_median_age_line_chart.jpg" width="650" height="400">

<img src="analyze_data/stock_price_mo_ratio_line_chart.jpg" width="650" height="400">

<img src="analyze_data/stock_price_middle_age_pop_line_chart.jpg" width="650" height="400">
