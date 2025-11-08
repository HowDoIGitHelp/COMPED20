# Midterms 2025

## Instructions

1. Download the dataset.
2. Follow the instructions below using Google Sheets or Orange Data Mining.

## Inspecting the dataset

1. Take note of the number of columns and rows.
2. Take note of the type of data for each column (qualitative or quantitative).

## Data Cleaning

1. Some of the columns in the dataset have missing values. Check which columns contain missing elements. Take note of the number of missing values for each column.
2. Delete rows that contain more than one missing value.
3. Impute the remaining missing values with the median of the column.

## Data Processing

1. Create the following columns:
    - `delayed` - quantitative, possible values: "Delayed", "Not Delayed". If the value found on the column, `actual_arrival_delay_min` is 5 minutes or more, then the `delayed` column should have the value "Delayed", otherwise it should have the value "Not Delayed".
    - `day_of_week` - qualitative, possible values: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". The day of the week for the date found on the column `date`
    - `hour_of_day` - quantitative, possible values: (0 - 23), the hour of the day in 24 hour format.
2. Export the extended dataset as a .csv file. The file name of the exported file should be "extended_public_transportation.csv"

## Changing granularity

1. Create a new dataset with a larger granularity. In this dataset, rows from "extended_public_transportation.csv" with the same date are summarized into one row.
2. The new dataset will have the following columns:
    - `date` - qualitative, the corresponding date of the row.
    - `weather_condition` - qualitative, the weather condition of that specific date. (use mode to summarize)
    - `mean_temperature_C` - quantitative, the mean temperature of all rows under the corresponding date. Keep the unit as Celcius.
    - `mean_humidity_percent` - quantitative, the mean humidity percentage of all rows under the corresponding date.
    - `mean_wind_speed_kmh` - quantitative, the mean wind speed of all rows under the corresponding date. Keep the unit as kmh.
    - `mean_precipitation_mm` - quantitative, the mean precipitation of all rows under the corresponding date. Keep the unit as mm.
    - `number_of_delays` - quantitative, the total number of delays for the corresponding date.
3. Export this new dataset as a .csv file. The file name of the exported file should be "daily_public_transportation_delays.csv"

## Declarative statistics

1. From "extended_public_transportation.csv", find the mean, median, and standard_deviation of the following quantitative columns: `temperature_C`, `humidity_percent`, `wind_speed_kmh`, `precipitation_mm`.
2. From "daily_public_transportation_delays.csv", find the mean, median, and standard deviation of `number_of_delays`.

## Grading Rubric
