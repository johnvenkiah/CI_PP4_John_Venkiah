import os
import requests


def get_lat_long_by_address(valid_address):
    lat, lng = None, None
    api_key = os.environ.get('GOOGLE_API_KEY')
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={valid_address}&key={api_key}"

    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    '''
    This try block incase any of our inputs are invalid. This is done
    instead of actually writing out handlers for all kinds of responses.
    '''
    results = r.json()['results'][0]
    lat = results['geometry']['location']['lat']
    lng = results['geometry']['location']['lng']

    return [lat, lng]
