from geopy.geocoders import Nominatim

def get_location(latitude, longitude):
    coordinates = latitude + ", " + longitude
    locator = Nominatim(user_agent="tynrGeocoder")
    location = locator.reverse(coordinates)
    
    # Nominatim returns None when unable to reverse geocode.
    if location is None:
        location_data = {
            "country": "n/a"
        }
    else:
        location_data = location.raw
        location_data = location_data["address"]
    
    return location_data
