import geocoder


def get_lat_long_by_address(valid_address):
    g = geocoder.google(valid_address)
    return [g.latlng[0], g.latlng[1]]


def get_city_by_lat_long(coords):
    city = [
        geocoder.google(
            [coord[0], coord[1]], method='reverse'
        ).city for coord in coords
    ]
    return city
