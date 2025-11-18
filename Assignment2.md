# Assignment 2 - Project proposals

The final project (which also corresponds to your final assessment grade) will require you to submit a data analytics project.
More details regarding the final project requirements will be posted in the future. 
For now, as an assignment, you and your assigned group will be compiling a list of project proposals for approval.
Here are the requirements for the proposals:

1. Source of the dataset (a link to the where the dataset was downloaded or the source where the data was acquired)
2. Description and background of the dataset
    - What do each sample in the dataset correspond to?
    - How was the data collected? (if this information is available)
3. Number of samples in the dataset
4. Number of features in the dataset
5. List of features, with descriptions for each feature
6. Insights you are interested in finding from the dataset

You will need to submit **at least three** proposals.

Here's an example proposal:

# Seoul Bike Sharing Demand Dataset

**Souurce**: UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand

**Description**: This is a dataset collected from a Seoul bike sharing service on Seoul Korea.
Each row in the dataset represents an hour rentals for the service.
The data is collected from a combination of bike sharing services and weather sensors.

**Number of samples**: 8760 samples

**Number of features**: 13 features

**Features**:
- Date: The corresponding date of the sample
- Rented Bike Count: The number of bike rentals for this hour.
- Hour: The hour of day (0 - 23) of the sample
- Temperature: The temperature measured for the hour
- Humidity: The humidity measured for the hour
- Wind speed: The wind speed measured for the hour
- Visibility: The visibility measured for the hour
- Dew point temperature: The dew point temp measured for the hour
- Solar Radiation: The solar radiation measured for the hour
- Rainfall: The rainfall measured for the hour
- Snowfall: The snowfall measured for the hour
- Season: The current season for the hour
- Functioning Day: whether or not the service was function during this day. (1 for a functioning day, 0 for a non-functioning day)

**Insights**:
- Which day of the week experience the highest demand of bike sharing rentals?
- Do bike rentals increase on colder weather?
- Do bike rentals increase on holidays?
