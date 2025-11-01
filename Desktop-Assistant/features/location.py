from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder, requests

def loc(place):
    place = place.replace("where", "")
    place = place.replace("is", "")
    place = place.replace("location", "")
    place = place.replace("from", "")
    place = place.replace("my", "")
    place = place.replace("of", "")
    place = place.replace("distance", "")
    place = place.replace(" ", "")
    
    geolocator = Nominatim(user_agent="Walter")
    location = geolocator.geocode(place, addressdetails=True)
    
    if location is None:
        return {"error": "Location not found"}, None, place
    
    target_latlng = location.latitude, location.longitude
    location_details = location.raw['address']
    target_loc = {'city': location_details.get('city', ''),
                  'state': location_details.get('state', ''),
                  'country': location_details.get('country', '')}

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)

    return target_loc, distance, place

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    
    return city, state, country
