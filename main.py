__author__ = 'Saleem Latif'
from geocode.geocode import GeoCode

if __name__ == "__main__":
    geo_code = GeoCode(address="Sydney, NSW")
    print geo_code
