import time
import math
from random import randrange
from . import env
import googlemaps

gmaps = googlemaps.Client(key=env.GOOGLE_API_KEY)


def calculate_offset(coordinates, dist, bearing):
    # calculates offset for sub_search
    # bearing: bearing in deg
    # returns new coordinates for sub_search
    new_bearing = math.radians(bearing)
    new_coord = dict(lng=None, lat=None)

    cos_offset = math.cos(new_bearing)
    sin_offset = math.sin(new_bearing)
    lat_bearing = math.cos(math.radians(coordinates['lat']))

    delta_lng = ((dist / 2) * cos_offset) / 111111
    delta_lat = (dist / 2) * (sin_offset / lat_bearing / 111111)

    new_coord['lat'] = coordinates['lat'] + delta_lat
    new_coord['lng'] = coordinates['lng'] + delta_lng

    return new_coord


def full_search(coordinates, dist, params):
    # full_search performs all 8 radial searches
    full_search_res = []

    for deg in range(0, 360, 45):
        search_coord = calculate_offset(coordinates, dist, deg)
        full_search_res.extend(sub_search(search_coord, dist / 2, params))

    return full_search_res


def sub_search(coordinates, dist, params):
    # search performs a single radial search
    # coord: user coordinates for location
    # type: dict
    # dist: search radius in meters
    # type: int
    # params: parameters for nearby_search
    # type: dict

    ret_list = []

    search_res = gmaps.places_nearby(location=coordinates, type='restaurant', radius=dist,
                                     min_price=params['min_price'],
                                     max_price=params['max_price'], keyword=params['cuisines'], open_now=True)

    if 'next_page_token' in search_res:
        next_token = search_res['next_page_token']
    else:
        next_token = None

    for result in search_res['results']:
        ret_list.append(
            dict(name=result['name'], address=result['vicinity'], type=result['types'], id=result['place_id']))

    if next_token is not None:
        time.sleep(2)
        search_res = gmaps.places_nearby(page_token=next_token)

        if 'next_page_token' in search_res:
            next_token = search_res['next_page_token']

        for result in search_res['results']:
            ret_list.append(
                dict(name=result['name'], address=result['vicinity'], type=result['types'], id=result['place_id']))

    if next_token is not None:
        time.sleep(2)
        search_res = gmaps.places_nearby(page_token=next_token)

        for result in search_res['results']:
            ret_list.append(
                dict(name=result['name'], address=result['vicinity'], type=result['types'], id=result['place_id']))

    return ret_list


def find_food(coordinates, dist, params):

    formatted_params = dict()

    if params['minPrice'] == '':
        formatted_params['min_price'] = None

    else:
        formatted_params['min_price'] = params['minPrice']

    if params['maxPrice'] == '':
        formatted_params['max_price'] = None

    else:
        formatted_params['max_price'] = params['maxPrice']

    if params['minPrice'] == '':
        formatted_params['min_price'] = None

    else:
        formatted_params['min_price'] = params['minPrice']

    if not params['cuisine']:
        formatted_params['keyword'] = None

    else:
        formatted_params['keyword'] = params['cuisine']

    # List of queried restaurants
    results = full_search(coordinates, dist, formatted_params)

    # Removes duplicate restaurants from results list
    filtered_res = [i for n, i in enumerate(results) if i not in results[n + 1:]]

    # Select random choice from filtered results list
    rand_choice = randrange(len(filtered_res))

    return filtered_res[rand_choice]
