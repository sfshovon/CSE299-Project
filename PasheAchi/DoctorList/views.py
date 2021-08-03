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

def doctor_list(request):
   
    timeStamp = database.child("Doctor").get()
    timeStampList = []
    for i in timeStamp.each():
        timeStampKey = i.key()
        timeStampList.append(timeStampKey)
    docName = []
    docSpecialty = []
    docEmail = []
    docImage = []
    docID = []
    for i in timeStampList:
        id = i
        fName = database.child("Doctor").child(i).child("docFName").get().val()
        lName = database.child("Doctor").child(i).child("docLName").get().val()
        name=fName + " " +lName 
        #docGender = database.child("Doctor").child(i).child("docGender").get().val()
        #docDesignation = database.child("Doctor").child(specialties).child(requid).child("designation").get().val()
        email = database.child("Doctor").child(i).child("docEmail").get().val()
        specialty = database.child("Doctor").child(i).child("docSpecializedField").get().val()
        image = database.child("Doctor").child(i).child("docImage").get().val()
        docID.append(id)
        docName.append(name)
        docSpecialty.append(specialty)   
        docEmail.append(email)  
        docImage.append(image)
    results = zip(docName, docSpecialty, docEmail, docImage, docID)  
        # Sending all data in zip form to doclist.html        
    return render(request,'docList/doclist.html',{"results": results})

def doctor_profile_view(request, keyy):
    fName = database.child("Doctor").child(keyy).child("docFName").get().val()
    lName = database.child("Doctor").child(keyy).child("docLName").get().val()
    Name=fName + " " +lName 
    image = database.child("Doctor").child(keyy).child("docImage").get().val()
    qualification = database.child("Doctor").child(keyy).child("docQualification").get().val()
    about = database.child("Doctor").child(keyy).child("About").get().val()
    designation = database.child("Doctor").child(keyy).child("docDesignation").get().val()
    email = database.child("Doctor").child(keyy).child("docEmail").get().val()
    workPlace = database.child("Doctor").child(keyy).child("docWorkingPlace").get().val()
    specialty = database.child("Doctor").child(keyy).child("docSpecializedField").get().val()
    consultationDays = database.child("Doctor").child(keyy).child("docConsultationDays").get().val()
    cNumber = database.child("Doctor").child(keyy).child("docNumber").get().val()
    hourOne = database.child("Doctor").child(keyy).child("docWorkingHour1").get().val()
    hourTwo = database.child("Doctor").child(keyy).child("docWorkingHour2").get().val()
    fees = database.child("Doctor").child(keyy).child("docConsultationFees").get().val()

    
    return render(request, 'docList/docprofile.html', {'docName':Name, 'docEmail':email, 'docImage':image, 'dWorkPlace':workPlace, 'dQualification':qualification, 'dAbout':about, 'dDesignation':designation, 'specializedField':specialty, 'cDays':consultationDays, 'timeOne':hourOne, 'timeTwo':hourTwo, 'CFees':fees, 'contact':cNumber })
    #return render(request, 'docList/docprofile.html', {'name':name, 'gender':docGender, 'specializedField':specialty,  'wPlace':workPlace,'timeOne':hourOne, 'timeTwo':hourTwo, 'CFees':fees, 'contact':cNumber,'docEmail':email})

    




   



    




