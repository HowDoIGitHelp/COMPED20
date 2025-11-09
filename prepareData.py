import pandas
import numpy as np



def corrupt(value): 
    rng = np.random.default_rng()
    randomFloat = rng.uniform(low=0.0, high=1.0)
    if randomFloat < 0.03:
        return np.nan
    else:
        return value

def normalOffsets(data, column_name, category, mean, std):
    rng = np.random.default_rng()
    selection = data[data[column_name] == category]
    return pandas.Series(np.round(rng.normal(loc=mean, scale=std, size=selection.shape[0])), index = selection.index).reindex(data.index, fill_value = 0).apply(int)

def main():
    rng = np.random.default_rng()
    data = pandas.read_csv("assets/Datasets/public_transport_delays.csv")

    data['scheduled_departure'] = pandas.to_datetime(data['date'] + " " + data['time'], format='%Y-%m-%d %H:%M:%S')
    data['peak_hour'] = data['scheduled_departure'].dt.hour.apply(lambda hour: 1 if (hour == 8 or hour == 18) else 0)

    data['actual_arrival_delay_min'] = pandas.Series(np.round(rng.normal(loc=0, scale=3, size=data.shape[0])), index=data.index)
    data['temperature_C'] = pandas.Series(np.round(rng.normal(loc=25, scale=5, size=data.shape[0]), decimals=2), index=data.index)
    data['humidity_percent'] = pandas.Series(np.round(rng.normal(loc=53, scale=5, size=data.shape[0]), decimals=2), index=data.index)
    data['precipitation_mm'] = pandas.Series(np.maximum(np.round(rng.normal(loc=2, scale=0.3, size=data.shape[0]), decimals=2), 0), index=data.index)
    data['wind_speed_kmh'] = pandas.Series(np.maximum(np.round(rng.normal(loc=15, scale=5, size=data.shape[0]), decimals=2), 0), index=data.index)

    data['delay_offset'] = -3

    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'weather_condition', 'Rain', 4, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'weather_condition', 'Storm', 15, 3)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'weather_condition', 'Snow', 9, 1)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'event_type', 'Concert', 7, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'event_type', 'Parade', 9, 3)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'event_type', 'Festival', 8, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'event_type', 'Sports', 4, 1)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'peak_hour', 1, 7, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'transport_type', 'Bus', 8, 10)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'transport_type', 'Tram', 1, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'origin_station', 'Station_9', 6, 2)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'origin_station', 'Station_10', 7, 1)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'origin_station', 'Station_11', 9, 4)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'origin_station', 'Station_12', -7, 4)
    data['delay_offset'] = data['delay_offset'] + normalOffsets(data, 'destination_station', 'Station_13', 15, 4)

    data['humidity_percent'] = data['humidity_percent'] + normalOffsets(data, 'weather_condition', 'Snow', -5, 1)
    data['temperature_C'] = data['temperature_C'] + normalOffsets(data, 'weather_condition', 'Snow', -20, 3)
    data['temperature_C'] = data['temperature_C'] + normalOffsets(data, 'weather_condition', 'Storm', -13, 4)
    data['temperature_C'] = data['temperature_C'] + normalOffsets(data, 'weather_condition', 'Rain', -5, 1)
    data['temperature_C'] = data['temperature_C'] + normalOffsets(data, 'weather_condition', 'Cloudy', -3, 1)
    data['precipitation_mm'] = data['precipitation_mm'] + normalOffsets(data, 'weather_condition', 'Snow', 13, 1)
    data['precipitation_mm'] = data['precipitation_mm'] + normalOffsets(data, 'weather_condition', 'Storm', 19, 7)
    data['precipitation_mm'] = data['precipitation_mm'] + normalOffsets(data, 'weather_condition', 'Rain', 4, 4)
    data['wind_speed_kmh'] = data['wind_speed_kmh'] + normalOffsets(data, 'weather_condition', 'Storm', 30, 5)
  #  data['precipitation_mm'] = data.apply(lambda row: rng.normal(loc = 1.0, scale = 2.0) if row['weather_condition'] == 'Clear' else row['precipitation_mm'], axis = 1)
  #  data['precipitation_mm'] = data.apply(lambda row: rng.normal(loc = 2.0, scale = 3.0) if row['weather_condition'] == 'Fog' else row['precipitation_mm'], axis = 1)
  #  data['precipitation_mm'] = data.apply(lambda row: rng.normal(loc = 2.5, scale = 3.0) if row['weather_condition'] == 'Cloudy' else row['precipitation_mm'], axis = 1)

    data['actual_arrival_delay_min'] = data['actual_arrival_delay_min'] + data['delay_offset']

    data['event_type'] = data['event_type'].fillna("No Event")

    weatherMeasurements = [
        "temperature_C", 
        "humidity_percent",
        "wind_speed_kmh",
        "precipitation_mm",
    ]

    for column in weatherMeasurements:
        data[column] = data[column].apply(corrupt)

    reducedData = data[[
        "trip_id", 
        "transport_type", 
        "origin_station", 
        "destination_station", 
        "actual_arrival_delay_min",
        "weather_condition",
        "temperature_C",
        "humidity_percent",
        "wind_speed_kmh",
        "precipitation_mm",
        "event_type",
        "peak_hour",
    ]]
    reducedData.to_csv("assets/Datasets/public_transportation_delays.csv", index=False)

if __name__ == "__main__":
    main()
