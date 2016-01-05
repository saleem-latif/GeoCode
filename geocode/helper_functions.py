import urllib

__author__ = 'Saleem Latif'


def encode_url(base_url, url_parameter_names, address='', lat='', lng='', key='',
               client='', signature='', **kwargs):

    url_parameters = {url_parameter_names['address']: address,
                      url_parameter_names['latlng']: "{lat}, {lng}".format(lat=lat, lng=lng),
                      url_parameter_names['key']: key,
                      url_parameter_names['client']: client,
                      url_parameter_names['signature']: signature,
                      }

    if client:
        del url_parameters[url_parameter_names['key']]
    else:
        del url_parameters[url_parameter_names['client']]
        del url_parameters[url_parameter_names['signature']]
    if address:
        del url_parameters[url_parameter_names['latlng']]
    else:
        del url_parameters[url_parameter_names['address']]

    if address and url_parameter_names['address'] in kwargs:
        del kwargs[url_parameter_names['address']]

    if lat and url_parameter_names['latlng'] in kwargs:
        del kwargs[url_parameter_names['latlng']]

    if lng and url_parameter_names['latlng'] in kwargs:
        del kwargs[url_parameter_names['latlng']]

    if key and url_parameter_names['key'] in kwargs:
        del kwargs[url_parameter_names['key']]

    if client and url_parameter_names['client'] in kwargs:
        del kwargs[url_parameter_names['client']]

    if signature and url_parameter_names['signature'] in kwargs:
        del kwargs[url_parameter_names['signature']]

    encode_url_parameters = urllib.urlencode(url_parameters) + "&" + urllib.urlencode(kwargs)

    return base_url + encode_url_parameters.rstrip("&")
