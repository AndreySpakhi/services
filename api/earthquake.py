import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
user_start_time = input("Enter the start time: ")
user_end_time = input("Enter the end time: ")
user_latitude = input("Enter the latitude: ")
user_longitude = input("Enter the longitude: ")
user_max_radius = input("Enter the max radius in km: ")
user_min_magnitude = input("Enter the min magnitude: ")

user_params = {
    'format': 'geojson',
    'starttime': user_start_time,
    'endtime': user_end_time,
    'latitude': user_latitude,
    'longitude': user_longitude,
    'maxradiuskm': user_max_radius,
    'minmagnitude': user_min_magnitude
}

response = requests.get(url, headers={'Accept': 'application/json'}, params=user_params)


data = response.json()
place_id = 1
for item in data['features']:
    print(f'{place_id}. Place: {item["properties"]["place"]}. Magnitude: {item["properties"]["mag"]}')
    place_id += 1
