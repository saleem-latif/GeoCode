__author__ = 'Saleem Latif'

import urllib2
from xml.etree import ElementTree

from constants import geo_code_url, google_url_parameter_names, STATUS_OK, STATUS_UNKNOWN, google_geocode_response_tags
from geocode_exceptions import APIError
from helper_functions import encode_url


class GeoCode():
    address = ''
    lat = ''
    lng = ''
    status = STATUS_UNKNOWN

    _key = ''
    _client = ''
    _signature = ''
    _url = ''
    _extra_url_parameters = {}

    def __init__(self, address='', lat='', lng='', key='', client='', signature='',  extra_url_parameters=''):

        if not (address or (lat and lng)):
            raise ValueError("No address or (lat, lng) given!")

        self.address = address
        self.lat = lat
        self.lng = lng
        self._key = key
        self._client = client
        self._signature = signature

        if extra_url_parameters:
            self._extra_url_parameters = extra_url_parameters

        self.update()

    def __str__(self):
        return "Address : " + self.address + "\n(lat, lng): (" + self.lat + ", " + self.lng + ")."

    def update(self, address='', lat='', lng='', extra_url_parameters=None):
        if (not (address or (lat and lng))) and (not (self.address or (self.lat and self.lng))):
            raise ValueError("No address or (lat, lng) given!")

        if extra_url_parameters and type(extra_url_parameters) is not dict:
            raise TypeError("Argument extra_url_parameters of type (%s) is not a dict" % type(extra_url_parameters))

        if address:
            self.address = address
        if lat:
            self.lat = lat
        if lng:
            self.lng = lng
        if extra_url_parameters:
            self._extra_url_parameters = extra_url_parameters

        self._url = encode_url(base_url=geo_code_url,
                               url_parameter_names=google_url_parameter_names,
                               address=self.address,
                               lat=self.lat,
                               lng=self.lng,
                               key=self._key,
                               client=self._client,
                               signature=self._signature,
                               **self._extra_url_parameters
                               )

        tree = self._get_xml_response_tree()
        self.address = tree.find(google_geocode_response_tags['address']).text
        self.lat = tree.find(google_geocode_response_tags['lat']).text
        self.lng = tree.find(google_geocode_response_tags['lng']).text

    def _get_xml_response_tree(self):
        reply = urllib2.urlopen(self._url)
        response_tree = ElementTree.parse(reply)

        self.status = response_tree.find(google_geocode_response_tags['status']).text
        self._validate_response()
        return response_tree

    def _validate_response(self):
        if self.status == u'OK':
            return STATUS_OK
        elif self.status == u'ZERO_RESULTS':
            raise APIError("Invalid Address, \n'ZERO_RESULTS' Returned by Google Maps")
        elif self.status == u'OVER_QUERY_LIMIT':
            raise APIError("You have exhausted your quota limits, \n'OVER_QUERY_LIMIT' Returned by Google Maps")
        elif self.status == u'REQUEST_DENIED':
            raise APIError("Your request was denied (Try including you API_KEY), "
                           "\n'REQUEST_DENIED' Returned by Google Maps")
        elif self.status == u'INVALID_REQUEST':
            raise APIError("Missing request parameters, \n'INVALID_REQUEST' Returned by Google Maps")
        elif self.status == u'UNKNOWN_ERROR':
            raise APIError("Internal Server Error, \n'UNKNOWN_ERROR' Returned by Google Maps")

    def get_address(self):
        if self.address:
            return self.address
        else:
            self.update()
            return self.address

    def get_lat(self):
        if self.lat:
            return self.lat
        else:
            self.update()
            return self.lat

    def get_lng(self):
        if self.lng:
            return self.lng
        else:
            self.update()
            return self.lng

    def get_latlng_tuple(self):
        if self.lat and self.lng:
            return self.lat, self.lng
        else:
            self.update()
            return self.lat, self.lng

    def get_latlng_list(self):
        if self.lat and self.lng:
            return [self.lat, self.lng]
        else:
            self.update()
            return [self.lat, self.lng]

    def get_latlng_dict(self):
        if self.lat and self.lng:
            return dict(lat=self.lat, lng=self.lng)
        else:
            self.update()
            return dict(lat=self.lat, lng=self.lng)

