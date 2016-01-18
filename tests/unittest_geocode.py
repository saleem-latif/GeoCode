from testscenarios import TestWithScenarios
import unittest
from geocode.geocode import GeoCodeAccessAPI


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
        self.api = GeoCodeAccessAPI()

    def test_geocode(self):
        if self.method == 'geocode':
            expected_address = self.address
            expected_lat = self.latlng[0]
            expected_lng = self.latlng[1]

            geocode = self.api.get_geocode(expected_address)

            self.assertAlmostEqual(geocode.lat, expected_lat, delta=5)
            self.assertAlmostEqual(geocode.lng, expected_lng, delta=5)
            self.assertIn(expected_address, geocode.address)

        else:
            expected_address = self.address
            expected_lat = self.latlng[0]
            expected_lng = self.latlng[1]

            address = self.api.get_address(lat=expected_lat, lng=expected_lng)
            self.assertIn(expected_address, address)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
