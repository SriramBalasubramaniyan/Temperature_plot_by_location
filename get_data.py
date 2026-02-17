import requests
from datetime import datetime, timedelta

def format_dates(input_date):
    return input_date.strftime("%Y-%m-%d") # format date in "YYYY-mm-dd"

def get_metro_data_by_location(latitude, longitude, days): 
    # gets lat and lng as parameters but default points to paris
    
    today = datetime.now() #current date
    target_date = today - timedelta(days=days) #week ago

    start_date = format_dates(target_date)
    end_date = format_dates(today)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    return response.json()