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
    params = req.GET #this is a dictionary
    print("Successfully read paramaters for request")
    #expected dictionary keys: cuisine, minPrice, maxPrice, radius, lon, lat, minRating, maxRating
    coordinates = dict(lng=float(params['lon']), lat=float(params['lat'])) #changed name to match exising funtion find_food
    d = params['radius']
    distance = d[0:d.find("mile")]
    print("Calling full_search")
    restaurant = searchfunctions.full_search(coordinates, int(distance), params) #this should return a JSON
    print("Getting detailed info")
    place_detailed = gmaps.place(gmaps, restaurant[id])
    json_res = json.dumps(place_detailed)
    return JsonResponse(json_res);
    
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
