# Midterms 2025

Please read all of the instructions before starting your work. 

To begin, download the dataset "public_transportation_delays.csv". You con work on the dataset using Google Sheets, Orange or both. When specifying filenames, column names, values, etc. make sure you are using the correct spelling.

## Inspecting the dataset

1. Take note of the number of columns and rows.
2. Take note of the type of data for each column (qualitative or quantitative).

## Data Cleaning

1. Some of the features in the dataset have missing values. Check which columns contain missing elements. Take note of the number of missing values for each column.
3. Impute the missing values with the mean (quantitative) and mode (qualitative) of their corresponding column.

## Data Processing

1. Create the following column:
    - `delayed` - quantitative, possible values: "Delayed", "Not Delayed". If the value found on the column, `actual_arrival_delay_min` is 5 minutes or more, then the `delayed` column should have the value "Delayed", otherwise it should have the value "Not Delayed".
2. Export the extended dataset as a .csv file. The file name of the exported file should be "extended_public_transportation.csv"

## Changing granularity

1. Create a new dataset with a larger granularity. In this dataset, rows from "extended_public_transportation.csv" with the same `origin_station` are summarized into one row.
2. The new dataset will have the following columns:
    - `origin_station` - qualitative, the corresponding origin station of the row.
    - `weather_condition` - qualitative, the weather condition of that specific station. (use mode to summarize)
    - `mean_temperature_C` - quantitative, the mean temperature of all rows of the corresponding station. Keep the unit as Celcius.
    - `mean_humidity_percent` - quantitative, the mean humidity percentage of all rows of the corresponding station.
    - `mean_wind_speed_kmh` - quantitative, the mean wind speed of all rows of the corresponding station. Keep the unit as kmh.
    - `mean_precipitation_mm` - quantitative, the mean precipitation of all rows of the corresponding station. Keep the unit as mm.
3. Export this new dataset as a .csv file. The file name of the exported file should be "station_weather.csv"

## Declarative statistics

1. From "extended_public_transportation.csv", find the mean, median, and standard_deviation of the following quantitative columns: `temperature_C`, `humidity_percent`, `wind_speed_kmh`, `precipitation_mm`.

## Insights from visualization

1. Create a box plot comparing the `actual_arrival_delay_min` of all `weather_condition`s, take note which weather conditions have the highest medians for `actual_arrival_delay_min`.
2. Create a box plot comparing the `actual_arrival_delay_min` of all `destination_station`s, take note which destination stations have the highest medians for `actual_arrival_delay_min`.
3. Create a scatter plot comparing the features `precipitation_mm` and `actual_arrival_delay_min`. 
4. Export the first box plot as an image and save the image as "box_plot_delays_vs_weather.png".
4. Export the second box plot as an image and save the image as "box_plot_delays_vs_station.png".
5. Export the scatter plot as an image and save the image a s "scatter_plot_precipitation_vs_delay.png"

## Grading Rubric

- 50% of your grade comes from your score in Part 2.
- 15% of your grade comes from your submission `extended_public_transportation.csv`
- 20% of your grade comes from your submission `station_weather.csv`
- 5% of your grade comes from your submission `box_plot_delays_vs_weather.csv`
- 5% of your grade comes from your submission `box_plot_delays_vs_station.csv`
- 5% of your grade comes from your submission `scatter_plot_precipitation_vs_delay.csv`
