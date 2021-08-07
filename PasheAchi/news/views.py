import requests
from django.shortcuts import render
import json

# Create your views here.

def news(request):

    url = "https://covid-19-news.p.rapidapi.com/v1/covid"

    querystring = {"q":"covid","lang":"en","media":"True","country":"BD","from":"2021/08/05"}

    headers = {
    'x-rapidapi-key': "3f65bbd635mshe1afe6cb1c3a5f3p1a2ff8jsn8a95a2d046e8",
    'x-rapidapi-host': "covid-19-news.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['articles']
    length = len(data)
    title = []
    summary = []
    articleLink = []
    websiteLink = []
    picture = []
    date = []
    for i in range(length):
        d=data[i]
        title.append(d['title'])
        summary.append(d['summary'])
        articleLink.append(d['link'])
        websiteLink.append(d['clean_url'])
        picture.append(d['media'])
        date.append(d['published_date'])
    
    newslist = zip(title, summary, articleLink, websiteLink, picture, date)  
        # Sending all data in zip form to news.html        
    return render(request, 'covidnews/news.html',{"newslist":newslist})