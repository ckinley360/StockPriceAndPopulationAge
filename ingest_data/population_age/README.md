# Data Sources

All population age data is sourced from the [United States Census Bureau website](https://www.census.gov/data.html). To get the entire population of the United States, I used the Resident Population plus Armed Forces Overseas. Data for different years is structured differently, and so I wrote custom Python scripts to ingest each unique data source.

- **1950 - 1979:** [Excel files](https://www.census.gov/data/tables/time-series/demo/popest/pre-1980-national.html). Annual estimate calculated in July.
- **1980 - 1989:** [Text files](https://www.census.gov/data/datasets/time-series/demo/popest/1980s-national.html) decoded with file layout specification. I used the July estimate for each year.
- **1990 - 1999:** [Population Estimates API](https://www.census.gov/data/developers/data-sets/popest-popproj/popest.1990-2000_Intercensals.html). Annual estimate calculated in April.
- **2000 - 2009:** [CSV file](https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-national.html).
