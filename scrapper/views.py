import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


def covid19_bd(request):
    """
    This covid19_bd method is used to scrap real time information about Bangladesh COVID19 Statistics from an API.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this covid19_bd method returns Bangladesh COVID19 statistics page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/Bangladesh/bgd"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff"
    }
        
    response = requests.request("GET", url, headers=headers).json()

    data = response
    length = len(data)
    country = []
    population = []
    tc = []
    nc = []
    ir = []
    cfr = [] 
    sc = []
    tdd = []
    nd = []
    trr = []
    nr = []
    rp = []
    ac = [] 
    tt = []
    tp = []
  
    for i in range(length):
        d=data[i]
        ir.append(d['Infection_Risk'])
        cfr.append(d['Case_Fatality_Rate']) 
        tp.append(d['Test_Percentage'])
        rp.append(d['Recovery_Proporation'])
        tc.append(d['TotalCases'])
        nc.append(d['NewCases'])
        tdd.append(d['TotalDeaths'])
        nd.append(d['NewDeaths'])
        trr.append(d['TotalRecovered'])
        nr.append(d['NewRecovered'])
        ac.append(d['ActiveCases'])
        tt.append(d['TotalTests'])
        population.append(d['Population'])
        sc.append(d['Serious_Critical'])
   
    covidUpdate = zip(population, tc, nc, ir, cfr, sc, tdd, nd, trr, nr, rp, ac, tt, tp)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/corona_scrapper_bd.html',{"covidUpdate":covidUpdate})  


def covid19_world(request):
    """
    This covid19_world method is used to scrap real time information about World COVID19 Statistics from an API.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this covid19_world method returns World COVID19 statistics page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/world"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff"
    }
            
    response = requests.request("GET", url, headers=headers).json()

    data = response
    length = len(data)
    country = []
    population = []
    tc = []
    nc = []
    ir = []
    cfr = [] 
    sc = []
    tdd = []
    nd = []
    trr = []
    nr = []
    rp = []
    ac = [] 
    tt = []
    tp = []
  
    for i in range(length):
        d=data[i]
        ir.append(d['Infection_Risk'])
        cfr.append(d['Case_Fatality_Rate']) 
        tp.append(d['Test_Percentage'])
        rp.append(d['Recovery_Proporation'])
        tc.append(d['TotalCases'])
        nc.append(d['NewCases'])
        tdd.append(d['TotalDeaths'])
        nd.append(d['NewDeaths'])
        trr.append(d['TotalRecovered'])
        nr.append(d['NewRecovered'])
        ac.append(d['ActiveCases'])
        tt.append(d['TotalTests'])
        population.append(d['Population'])
        sc.append(d['Serious_Critical'])
   
    covidUpdate = zip(population, tc, nc, ir, cfr, sc, tdd, nd, trr, nr, rp, ac, tt, tp)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/corona_scrapper_world.html',{"covidUpdate":covidUpdate})   

def country_cases(request):
    """
    This country_cases method is used to scrap real time information aboutt All Countries COVID19 Statistics from an API.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this country_cases method returns COVID19 cases by countries page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "dd340330f0mshbe4a15b45995ce0p181f6djsn73e74731beff"
    }
        
    response = requests.request("GET", url, headers=headers).json()

    data = response
    length = len(data)
    country = []
    population = []
    tc = []
    nc = []
    ir = []
    cfr = [] 
    sc = []
    tdd = []
    nd = []
    trr = []
    nr = []
    rp = []
    ac = [] 
    tt = []
    tp = []
  
    for i in range(length):
        d=data[i]
        country.append(d['Country'])
        ir.append(d['Infection_Risk'])
        cfr.append(d['Case_Fatality_Rate']) 
        tp.append(d['Test_Percentage'])
        rp.append(d['Recovery_Proporation'])
        tc.append(d['TotalCases'])
        nc.append(d['NewCases'])
        tdd.append(d['TotalDeaths'])
        nd.append(d['NewDeaths'])
        trr.append(d['TotalRecovered'])
        nr.append(d['NewRecovered'])
        ac.append(d['ActiveCases'])
        tt.append(d['TotalTests'])
        population.append(d['Population'])
        sc.append(d['Serious_Critical'])
   
    covidUpdate = zip(country, population, tc, nc, ir, cfr, sc, tdd, nd, trr, nr, rp, ac, tt, tp)  
    # Sending all data in zip form to vaccine_news.html            
    return render(request, 'scrapper/country_cases.html',{"covidUpdate":covidUpdate}) 

def all_treatments(request):
    """
    This all_treatments method is used to scrap real time information about all the treatments for COVID19 from an API.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this all_treatments method returns all COVID19 treatment list page
    which is a HTML page.

    :rtype: HttpResponse.
    """
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
    return render(request, 'scrapper/treatments_list.html',{"all":allTreatmentList })

def all_vaccines(request):
    """
    This all_vaccines method is used to scrap real time information about all the vaccines for COVID19 from an API.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this all_vaccines method returns all COVID19 vaccines list page
    which is a HTML page.

    :rtype: HttpResponse.
    """
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
    return render(request, 'scrapper/vaccines_list.html',{"all":allVaccinesList})

def ambulance(request):
    """
    This ambulance method is used to show information about ambulance services name and contact of Bangladesh.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this ambulance method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/ambulance.html')

def covid_hotline(request):
    """
    This covid_hotline method is used to show information about Bangladesh COVID19 Hotline services.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this covid_hotline method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/covid_hotline.html')

def test_center(request):
    """
    This test_center method is used to show information about Bangladesh COVID19 Test Centers.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this test_center method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/test_center.html')

def test_place(request):
    """
    This test_place method is used to show information about Bangladesh COVID19 Test Instituitions.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this test_place method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/test_place.html')

def oxygen_cylinder(request):
    """
    This oxygen_cylinder method is used to show information about oxygen cylinder services in Bangladesh.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this oxygen_cylinder method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/oxygen_cylinder.html')

def icu_bed(request):
    """
    This icu_bed method is used to show information about icu_bed numbers in each hospital in Bangladesh.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this icu_bed method returns a static page
    which is a HTML page.

    :rtype: HttpResponse.
    """
    return render(request, 'scrapper/icu_bed_list.html')

   
