from django.shortcuts import render
#from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pyrebase
import os

config={
    "apiKey": "AIzaSyCR1mvz5oDzyUfC6fk_Y56mgGXy7uVawCY",
    "authDomain": "pashe-achi-cse299.firebaseapp.com",
    "databaseURL": "https://pashe-achi-cse299-default-rtdb.firebaseio.com/",
    "projectId": "pashe-achi-cse299",
    "storageBucket": "pashe-achi-cse299.appspot.com",
    "messagingSenderId": "798613820174",
    "appId": "1:798613820174:web:8d03f5cf0fbae3e9dcbd5f",
    "measurementId": "G-TZN8WC3LJT"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()
database = firebase.database()
# Create your views here.

def search_blog_post(request):
    if request.method == "POST" and "csrfmiddlewaretoken" in request.POST:
        keyword = request.POST.get('search')
        keyword = keyword.lower()
        requid = []
        userName = []
        post = []
        posts = []
        # initializing punctuations string
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        id = database.child("Blog Post").get()
        idList = []
        for i in id.each():
            idKey = i.key()
            idList.append(idKey)
        for i in idList:
            blog = database.child("Blog Post").child(i).child("post").get().val()
            post = blog.lower()
            for ele in post:
                if ele in punc:
                    post = post.replace(ele, "")
            dict = post.split()
            for word in dict:
                if(word==keyword):
                    requid.append(i) 
                    break
        print(requid)

        if(len(requid)==0):
            return render(request, "search/searchnotfound.html")
        else:
            for i in requid:
                name = database.child("Blog Post").child(i).child("fullName").get().val()
                searchPost = database.child("Blog Post").child(i).child("post").get().val()
                userName.append(name)
                posts.append(searchPost)

            results = zip(userName, posts)
            return render(request,'search/search.html',{"results": results})

def search_not_found(request):
    return render(request, "search/searchnotfound.html")
