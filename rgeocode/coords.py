from geopy.geocoders import Nominatim

def get_location(latitude, longtitude):
    coordinates = latitude + ", " + longtitude
    locator = Nominatim(user_agent="tynrGeocoder")
    location = locator.reverse(coordinates)
    location_data = location.raw
    location_data = location_data["address"]
    
    return location_data
