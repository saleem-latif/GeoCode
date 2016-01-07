import urllib
import urlparse


def encode_geocode_url(base_url, parameter_names_map, address='', lat='', lng='', key='',
                       client='', signature='', **kwargs):

    url_parameters = {
        parameter_names_map['address']: address,
        parameter_names_map['latlng']: "{lat}, {lng}".format(lat=lat, lng=lng),
        parameter_names_map['key']: key,
        parameter_names_map['client']: client,
        parameter_names_map['signature']: signature,
    }

    if client:
        # if client is resent we do not want to use key for geocode lookup.
        del url_parameters[parameter_names_map['key']]
    else:
        del url_parameters[parameter_names_map['client']]
        del url_parameters[parameter_names_map['signature']]

    if address:
        del url_parameters[parameter_names_map['latlng']]
    else:
        del url_parameters[parameter_names_map['address']]

    if address and parameter_names_map['address'] in kwargs:
        del kwargs[parameter_names_map['address']]

    if lat and parameter_names_map['latlng'] in kwargs:
        del kwargs[parameter_names_map['latlng']]

    if lng and parameter_names_map['latlng'] in kwargs:
        del kwargs[parameter_names_map['latlng']]

    if key and parameter_names_map['key'] in kwargs:
        del kwargs[parameter_names_map['key']]

    if client and parameter_names_map['client'] in kwargs:
        del kwargs[parameter_names_map['client']]

    if signature and parameter_names_map['signature'] in kwargs:
        del kwargs[parameter_names_map['signature']]

    url_parameters.update(kwargs)
    return encode_url(base_url, url_parameters)


def encode_url(base_url, params):
    url_parts = list(urlparse.urlparse(base_url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urllib.urlencode(query)

    return urlparse.urlunparse(url_parts)
