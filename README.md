# Stock Price And Population Age
A high-level analysis of the relationship between U.S. stock prices and U.S. age demographics.

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)

## General Information
According to [Investopedia](https://www.investopedia.com/articles/basics/04/100804.asp#:~:text=traders%20and%20investors.-,Fundamental%20Factors,as%20a%20P%2FE%20ratio), there are three categories of forces that affect stock prices - fundamental factors, technical factors, and market sentiment. Of these three forces, I find technical factors to be the most interesting, specifically age demographics. With [reports](https://www.bbc.com/news/world-us-canada-57003722) of the U.S. birth rate declining (along with many other countries), I was curious what impact, if any, it might have on the stock market. To explore the potential relationship between stock prices and age demographics, I compared historical inflation-adjusted close prices of the S&P 500 with U.S. population age data for the years 1950-2020.

The S&P 500 index is widely seen as representative of the health of the U.S. economy, and since I'm interested in analyzing stock prices at a macro-level, it seemed like a great choice. I used inflation-adjusted close prices to eliminate inflation as a factor for the change in close prices so that I could have an "apples-to-apples" comparison over time. [multpl](https://www.multpl.com/inflation-adjusted-s-p-500/table/by-year) has a nice table of historical inflation-adjusted S&P 500 close prices, and this is the source of the stock price data that I used.

The [U.S. Census Bureau](https://www.census.gov/data.html) has a treasure trove of publicly available demographic data, including the estimated population of the U.S. over time, broken down by single year of age. This is the source of the age data that I used.

## Technologies Used
- Python 3.10.2 for data ingestion, transformation, and analysis

<img src="analyze_data/stock_price_median_age_line_chart.jpg" width="650" height="400">

<img src="analyze_data/stock_price_mo_ratio_line_chart.jpg" width="650" height="400">

<img src="analyze_data/stock_price_middle_age_pop_line_chart.jpg" width="650" height="400">
