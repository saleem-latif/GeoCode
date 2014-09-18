__author__ = 'Saleem Latif'

from testscenarios import TestWithScenarios
import unittest
from geocode.geocode import GeoCode


class GeoCodeTests(TestWithScenarios, unittest.TestCase):

    scenarios = [("Scenario - 1: Get latlng from address",
                  {'address': "Sydney NSW",
                   'latlng': (-33, 151),
                   'method': "geocode"
                   }
                  ),

                 ]

    def setUp(self):
        pass

    def test_geocode(self):
        if self.method == 'geocode':
            expected_address = self.address
            expected_lat = self.latlng[0]
            expected_lng = self.latlng[1]

            geo_code = GeoCode(address=expected_address)
        else:
            expected_address = self.address
            expected_lat = self.latlng[0]
            expected_lng = self.latlng[1]

            geo_code = GeoCode(lat=expected_lat, lng=expected_lng)

        lat = int(float(geo_code.get_lat()))
        lng = int(float(geo_code.get_lng()))
        address = geo_code.get_address()

        assert (lat, lng) == (expected_lat, expected_lng), "(" + str(lat) + ", " + str(lng) + \
                                                           ") returned by GeoCode is not same as" + "(" + \
                                                           str(expected_lat) + ", " + str(expected_lng) + ")"

        assert expected_address in address, "Address: " + str(address) + "\nas returned by GeoCode is not same as " + \
                                            expected_address

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()