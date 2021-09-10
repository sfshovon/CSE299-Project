from django.shortcuts import render
#from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pyrebase
import difflib
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
def search_page(request):
    """
        This method is used to render the search for blog posts page.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the search page.

        :rtype: HttpResponse.
    """ 
    return render(request,'search/search_page.html') 

def search_blog_post(request):
    """
        This method is used to search for a blog post by entering a keyword.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the search results based on the keyword.

        :rtype: HttpResponse.
    """ 
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
            request.session['word'] = keyword
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
    """
        This method is used to display the search not found page.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the search not found page.

        :rtype: HttpResponse.
    """  
    return render(request,'search/searchnotfound.html')   

def search_doctors(request): 
    """
        This method is used to search for doctors by entering their name.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the doctor card based on the search.

        :rtype: HttpResponse.
    """  
    if request.method == "POST" and "csrfmiddlewaretoken" in request.POST:
        keyword = request.POST.get('search_doc')
        keyword = keyword.lower()
        id = database.child("Doctor").get()
        idList = []
        requid = None
        for i in id.each():
            idKey = i.key()
            idList.append(idKey)
        for i in idList:
            fName = database.child("Doctor").child(i).child("docFName").get().val()
            lName = database.child("Doctor").child(i).child("docLName").get().val()
            fName = fName.lower()
            lName = lName.lower()
            name=fName + " " +lName
            name = name.lower()
            print(name, fName, lName, keyword)
            if (name == keyword):
                requid = i
                break  
            elif (fName == keyword):
                requid = i
                break
            elif (lName == keyword):
                requid = i
                break 
        if (requid is not None): 
            fName = database.child("Doctor").child(requid).child("docFName").get().val()
            lName = database.child("Doctor").child(requid).child("docLName").get().val()
            docName=fName + " " +lName
            docSpecialty = database.child("Doctor").child(requid).child("docSpecializedField").get().val()
            docEmail = database.child("Doctor").child(requid).child("docEmail").get().val()
            docImage = database.child("Doctor").child(requid).child("docImage").get().val()           
            return render(request,'search/search_doctors.html',{'docID':requid,'docName':docName, 'docSpecialty':docSpecialty, 'docEmail':docEmail, 'docImage':docImage})
        else:
            return render(request,'search/searchnotfound.html')
 

   
