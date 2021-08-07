import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


def covid19_bd(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Bangladesh"}

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    d = response['response']
    s = d[0]
    
    context = {
        'all': s['cases']['total'],
        'tests': s['tests']['total'],
        'test': s['tests']['1M_pop'],
        'active': s['cases']['active'],
        'new': s['cases']['new'],
        'recovered': s['cases']['recovered'],
        'serious': s['cases']['critical'],
        'deaths': s['deaths']['total'],
        'death': s['deaths']['new'],
        
    }
    
    return render(request, 'scrapper/corona_scrapper_bd.html', context)


def covid19_world(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"All"}
    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    d = response['response']
    s = d[0]
    context = {
        'all': s['cases']['total'],
        'active': s['cases']['active'],
        'new': s['cases']['new'],
        'recovered': s['cases']['recovered'],
        'serious': s['cases']['critical'],
        'deaths': s['deaths']['total'],
        'death': s['deaths']['new'],
    }
    return render(request, 'scrapper/corona_scrapper_world.html', context)
