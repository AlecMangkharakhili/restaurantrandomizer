from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.http import HttpResponse
import json
from . import searchfunctions
from . import env
import googlemaps

gmaps = googlemaps.Client(key=env.GOOGLE_API_KEY)

# Create your views here.

def findfood(req):
    params = HttpRequest.content_params #this is a dictionary
    #expected dictionary keys: cuisine, minPrice, maxPrice, radius, lon, lat, minRating, maxRating
    coordinates = dict(lng=params['lon'], lat=params['lat']) #changed name to match exising funtion find_food
    params.remove('lon')
    params.remove('lat')
    restaurant = searchfunctions.full_search(coordinates, params['radius'], params) #this should return a JSON
    return JsonResponse(restaurant);
    
def ping_request(req):
    return JsonResponse({'response': 'body'})
    
def findfood_old(req):
    req_params = json.loads(req.body.decode('utf-8'))

    coord = dict(location=dict(lat=req_params['data']['long'], lng=req_params['data']['lat']))

    dist = (int(req_params['data']['radius']) * 1609.34)
    search_params = dict(min_price=req_params['data']['price_min'], max_price=req_params['data']['price_max'],
                         min_rating=req_params['data']['rating_min'], max_rating=req_params['data']['rating_max'],
                         keyword=req_params['data']['type'])

    restaurant = searchfunctions.find_food(coord['location'], dist, search_params)

    place_detailed = gmaps.place(gmaps, restaurant[id])

    json_res = json.dumps(place_detailed)

    return JsonResponse({'res': json_res})
