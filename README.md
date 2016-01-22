GeoCode
=======

Python wrapper for google's geoode REST API

GeoCode allows you to retrieve latitude longitude for an address or vice versa.

__Setup:__

Follow these steps to setup GeoCode locally.

* Clone GeoCode repository `git clone https://github.com/saleem-latif/GeoCode.git`
* Create and activate [virtual environment](https://virtualenv.readthedocs.org/en/latest/userguide.html).
* install requirements `pip install -r geocode/requirements.txt`
* run tests `python geocode/tests/unittest_geocode.py`

__Example Usage:__

`geo_code = GeoCodeAccessAPI(address="Sydney, NSW")`

__Accessing latitude/longitude or Address:__

`lat = geo_code.lat`

`lng = geo_code.lng`

`address = geo_code.address`
