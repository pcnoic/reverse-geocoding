## Tynr.io Reverse Geocoder

### Overview 

Tiny API developed in Python with FastAPI for reverse geocoding. Utilizing data from OpenStreetMaps with Naminator. 

### Usage

You can get the country name and country code of a pair of coordinates by sending the following request. 

```
curl --location --request POST 'http://<api-address>:<api-port>/georeverse/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "latitude": "-14.827479",
    "longtitude": "-77.639729"
}'
```

The expected response is:

```
{
    "country": "Perú",
    "country_code": "pe"
}
```