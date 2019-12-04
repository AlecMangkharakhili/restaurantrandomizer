from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from . import searchfunctions


# Create your views here.

def findfood(req):
    params = HttpRequest.content_params #this is a dictionary
    
    
    
def ping_request(req):
    print("ping request received from:", req.META.get("REMOTE_ADDR"))
    html = "<html><body>The server has been pinged.</body></html>"
    return HttpResponse(html)
    
def findfood_old(req):
    req_params = json.loads(req.body.decode('utf-8'))

    coord = dict(location=dict(lat=req_params['data']['long'], lng=req_params['data']['lat']))

    dist = (int(req_params['data']['radius']) * 1609.34)
    search_params = dict(min_price=req_params['data']['price_min'], max_price=req_params['data']['price_max'],
                         min_rating=req_params['data']['rating_min'], max_rating=req_params['data']['rating_max'],
                         keyword=req_params['data']['type'])

    restaurant = searchfunctions.find_food(coord['location'], dist, search_params)

    json_res = json.dumps(restaurant)

    return JsonResponse({'res': json_res})
