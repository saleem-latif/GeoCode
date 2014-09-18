__author__ = 'Saleem Latif'

geo_code_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'

google_url_parameter_names = dict(address='address',
                                  latlng='latlng',
                                  key='key',
                                  client='client',
                                  signature='signature',
                                  )

google_geocode_response_tags = dict(status='status',
                                    address='result/formatted_address',
                                    location='location',
                                    lat='result/geometry/location/lat',
                                    lng='result/geometry/location/lng',
                                    result='result'
                                    )

# Response Status Codes
STATUS_OK = "Status OK"
STATUS_ERROR = "Status Error"
STATUS_UNKNOWN = "Status Unknown"

