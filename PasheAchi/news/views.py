from django.shortcuts import render

def news(request):
    return render(request, 'covidnews/news.html')
