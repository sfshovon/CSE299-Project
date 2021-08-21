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
    return render(request, 'scrapper/corona_scrapper_world.html',context)

def news(request):
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-health-news/0"

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()
    data = response['news']
    length = len(data)
    title = []
    articleLink = []
    picture = []
    date = []
    content = []
    
    for i in range(length):
        d=data[i]
        title.append(d['title'])
        articleLink.append(d['link'])
        picture.append(d['urlToImage'])
        date.append(d['pubDate'])
        content.append(d['content'])
        
    vaccineNewsList = zip(title, articleLink, picture, date, content)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/news.html',{"vaccineNews":vaccineNewsList})

def FDA_approved_vaccines(request):
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-fda-approved-vaccines"

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()

    #print(response.text)
    data = response
    length = len(data)
    name = []
    trimedName = []
    category = []
    trimedCategory = []
    phase = []
    nextSteps = []
    description = []
    funder = []
    FDAApproved = []
    lastUpdated = []

    for i in range(length):
        d=data[i]
        name.append(d['developerResearcher'])
        trimedName.append(d['trimedName'])
        category.append(d['category'])
        trimedCategory.append(d['trimedCategory'])
        phase.append(d['phase'])
        nextSteps.append(d['nextSteps'])
        description.append(d['description'])
        funder.append(d['funder'])
        FDAApproved.append(d['FDAApproved'])
        lastUpdated.append(d['lastUpdated'])
        
    fdaApprovedVaccinesList = zip(name,trimedName, category, trimedCategory, phase, nextSteps, description, funder, FDAApproved, lastUpdated)  
    # Sending all data in zip form to vaccine_news.html         
    
    return render(request, 'scrapper/all.html',{"all":fdaApprovedVaccinesList})


def FDA_approved_treatments(request):
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-fda-approved-treatment"

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()

    #print(response.text)
    data = response
    length = len(data)
    name = []
    trimedName = []
    category = []
    trimedCategory = []
    phase = []
    nextSteps = []
    description = []
    funder = []
    FDAApproved = []
    lastUpdated = []

    for i in range(length):
        d=data[i]
        name.append(d['developerResearcher'])
        trimedName.append(d['trimedName'])
        category.append(d['category'])
        trimedCategory.append(d['trimedCategory'])
        phase.append(d['phase'])
        nextSteps.append(d['nextSteps'])
        description.append(d['description'])
        funder.append(d['funder'])
        FDAApproved.append(d['FDAApproved'])
        lastUpdated.append(d['lastUpdated'])
        
    fdaApprovedTreatmentsList = zip(name,trimedName, category, trimedCategory, phase, nextSteps, description, funder, FDAApproved, lastUpdated)  
    # Sending all data in zip form to vaccine_news.html         
    
    return render(request, 'scrapper/all.html',{"all":fdaApprovedTreatmentsList})

def all_treatments(request):
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-treatment"

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers).json()

    #print(response.text)
    data = response
    length = len(data)
    name = []
    trimedName = []
    category = []
    trimedCategory = []
    phase = []
    nextSteps = []
    description = []
    funder = []
    FDAApproved = []
    lastUpdated = []

    for i in range(length):
        d=data[i]
        name.append(d['developerResearcher'])
        trimedName.append(d['trimedName'])
        category.append(d['category'])
        trimedCategory.append(d['trimedCategory'])
        phase.append(d['phase'])
        nextSteps.append(d['nextSteps'])
        description.append(d['description'])
        funder.append(d['funder'])
        FDAApproved.append(d['FDAApproved'])
        lastUpdated.append(d['lastUpdated'])
        
    allTreatmentList = zip(name,trimedName, category, trimedCategory, phase, nextSteps, description, funder, FDAApproved, lastUpdated)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/all.html',{"all":allTreatmentList })

def all_vaccines(request):
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-vaccines"

    headers = {
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers).json()

    #print(response.text)
    data = response
    length = len(data)
    name = []
    trimedName = []
    category = []
    trimedCategory = []
    phase = []
    nextSteps = []
    description = []
    funder = []
    FDAApproved = []
    lastUpdated = []

    for i in range(length):
        d=data[i]
        name.append(d['developerResearcher'])
        trimedName.append(d['trimedName'])
        category.append(d['category'])
        trimedCategory.append(d['trimedCategory'])
        phase.append(d['phase'])
        nextSteps.append(d['nextSteps'])
        description.append(d['description'])
        funder.append(d['funder'])
        FDAApproved.append(d['FDAApproved'])
        lastUpdated.append(d['lastUpdated'])
        
    allVaccinesList = zip(name,trimedName, category, trimedCategory, phase, nextSteps, description, funder, FDAApproved, lastUpdated)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/all.html',{"all":allVaccinesList})
