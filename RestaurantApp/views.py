from django.shortcuts import render
from django.http import JsonResponse
import json
from . import searchfunctions


# Create your views here.

def findfood(req):
    req_params = json.loads(req.body.decode('utf-8'))

    coord = dict(location=dict(lat=req_params['data']['long'], lng=req_params['data']['lat']))

    dist = (int(req_params['data']['radius']) * 1609.34)
    search_params = dict(min_price=req_params['data']['price_min'], max_price=req_params['data']['price_max'],
                         min_rating=req_params['data']['rating_min'], max_rating=req_params['data']['rating_max'],
                         keyword=req_params['data']['type'])

    restaurant = searchfunctions.find_food(coord['location'], dist, search_params)

    json_res = json.dumps(restaurant)

    return JsonResponse({'res': json_res})
