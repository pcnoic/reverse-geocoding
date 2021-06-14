## Tynr.io Reverse Geocoder

### Overview 

Tiny API developed in Python with FastAPI for reverse geocoding. Utilizing data from OpenStreetMaps with Naminator. 

### Usage

#### Example request

```
curl --location --request POST 'http://<api-address>:<api-port>/georeverse/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "latitude": "-14.827479",
    "longtitude": "-77.639729"
}'
```

#### Example responses

The API has 3 general return cases based on the input that it receives. 

##### Case 1
The coordinates that you've sent in your POST request are not linked to a known area.

Response:

```json
{
    "country":"n/a"
}
```

##### Case 2
The coordinates that you've sent in your POST request are linked to a country but no more specific data can be acquired.

Response:

```json
{
    "country": "Perú",
    "country_code": "pe"
}
```

##### Case 3
The coordinates that you've sent in your POST request are linked to a country and further information about the address can be acquired.

Response:
```json
{
    "house_number": "66",
    "road": "Αγίου Δημητρίου",
    "suburb": "Διοικητήριο",
    "city_district": "2η Κοινότητα Θεσσαλονίκης",
    "city": "Δημοτική Ενότητα Θεσαλονίκης",
    "municipality": "Δήμος Θεσσαλονίκης",
    "county": "Περιφερειακή Ενότητα Θεσσαλονίκης",
    "state_district": "Περιφέρεια Κεντρικής Μακεδονίας",
    "state": "Αποκεντρωμένη Διοίκηση Μακεδονίας - Θράκης",
    "postcode": "54123",
    "country": "Ελλάς",
    "country_code": "gr"
}
```