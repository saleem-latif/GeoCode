from testscenarios import TestWithScenarios
import unittest
from geocode.geocode import GeoCode


class GeoCodeTests(TestWithScenarios, unittest.TestCase):

    scenarios = [
        (
            "Scenario - 1: Get latlng from address",
            {
                'address': "Sydney NSW",
                'latlng': (-33.8674869, 151.2069902),
                'method': "geocode",
            }
        ),
        (
            "Scenario - 2: Get address from latlng",
            {
                'address': "Sydney NSW",
                'latlng': (-33.8674869, 151.2069902),
                'method': "address",
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

        lat = int(float(geo_code.lat))
        lng = int(float(geo_code.lng))
        address = geo_code.address

        self.assertAlmostEqual(lat, expected_lat, delta=5)
        self.assertAlmostEqual(lng, expected_lng, delta=5)
        self.assertIn(expected_address, address)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
