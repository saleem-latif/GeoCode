GeoCode
=======

Python wrapper for google's geoode REST API

GeoCode allows you to retrieve latitude longitude for an address or vice cersa.

Example:

geo_code = GeoCode(address="Sydney, NSW")

lat = geo_code.get_lat()
lng = geo_code.get_lng()
address = geo_code.get_address()

Note:
  Code need to be tested docuk=mented properly.
  
