import matplotlib.pyplot as plt
import tabulate
import os
from get_data import get_metro_data_by_location
from geopy.geocoders import Nominatim

def get_weather_data(latitude, longitude, days):
    data = get_metro_data_by_location(latitude, longitude, days) #get metro data

    df = tabulate.get_df(data) # fetch data frame details created using panda

    #find location name using geolcator with lat and lng points
    geolocator = Nominatim(user_agent ="geo_api")
    city_name = geolocator.reverse(f"{latitude},{longitude}")

    #create plot
    plt.figure(figsize=(10,6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    #set labels
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"{city_name} Weather - Past {days} Days")
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Create data folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save the plot in data folder
    plt.savefig(f'data/{city_name}_weather_chart.png')
    plt.show()

    # Save to CSV
    df.to_csv(f'data/{city_name}_weather.csv', index=False)
    print(f"Data saved to data/{city_name}_weather.csv")


get_weather_data(latitude = 11.164981, longitude = 77.345887, days=30) 
# be carefull of days the api to get data only support upto 3 month past data
# https://www.latlong.net/ use this site to get lat and lng data