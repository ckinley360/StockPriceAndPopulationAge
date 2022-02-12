# Data Sources

All population age data is sourced from the [United States Census Bureau website](https://www.census.gov/data.html). To get the entire population of the United States, I used the Estimated Resident Population plus Armed Forces Overseas. To be able to create my own age ranges, I used the population estimates that are broken down by Single Year of Age. Data for different years is structured differently, and so I wrote custom Python scripts to ingest each unique data source.

- **1950 - 1979:** [Excel files](https://www.census.gov/data/tables/time-series/demo/popest/pre-1980-national.html). Annual estimate calculated in July.
- **1980 - 1989:** [Text files](https://www.census.gov/data/datasets/time-series/demo/popest/1980s-national.html) decoded with file layout specification. I used the July estimate for each year.
- **1990 - 1999:** [Population Estimates API](https://www.census.gov/data/developers/data-sets/popest-popproj/popest.1990-2000_Intercensals.html). Annual estimate calculated in April.
- **2000 - 2010:** [CSV file](https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-national.html). I used the July estimate for each year.
- **2011 - 2020:** [CSV files](https://www.census.gov/data/tables/time-series/demo/popest/2010s-national-detail.html). I used the July estimate for each year.

To verify that I pulled the data correctly, I used the [Federal Reserve Bank of St. Louis's population data](https://fred.stlouisfed.org/graph/?id=POP,) as a cross-check. There are some small differences due to the St. Louis Fed's rounding, and potentially pulling data from a United States Census Bureau source that was calculated in a slightly different way (you can get population estimates for the same date range in multiple places on the Census Bureau's website).

# Data Normalization

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
