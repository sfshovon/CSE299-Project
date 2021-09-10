from django.shortcuts import render
import pyrebase
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
def view_icu_beds(request):
    """
        This method is used to display the list of available ICU beds.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the list of ICU beds along with their availability statuses.

        :rtype: HttpResponse.
    """ 
    timeStamp = database.child("ICU").get()
    timeStampList = []
    for i in timeStamp.each():
        timeStampKey = i.key()
        timeStampList.append(timeStampKey)
    hosName = []
    totalBeds = []
    availableBeds = []
    icuID = []
    for i in timeStampList:
        id = i
        name = database.child("ICU").child(i).child("hosName").get().val()  
        total = database.child("ICU").child(i).child("total").get().val()
        available = database.child("ICU").child(i).child("available").get().val()     
        icuID.append(id) 
        hosName.append(name)
        totalBeds.append(total)   
        availableBeds.append(available)  
    print(totalBeds)   
    print(availableBeds)
    results = zip(hosName, totalBeds, availableBeds, icuID)  
        # Sending all data in zip form to icubed.html        
    return render(request, 'icu/icubed.html',{"results": results})

def icu_details(request, keyy):
    """
        This method is used to display the details of a specific icu bed.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the details along with the location of the icu.

        :rtype: HttpResponse.
    """  
    name = database.child("ICU").child(keyy).child("hosName").get().val()  
    location = database.child("ICU").child(keyy).child("location").get().val()  
    hosContact = database.child("ICU").child(keyy).child("contact").get().val()
    webLink = database.child("ICU").child(keyy).child("website").get().val() 
    mapLink = database.child("ICU").child(keyy).child("map").get().val() 
    return render(request, 'icu/icu_details.html', {'hosName':name, 'hosLocation':location, 'contact':hosContact, 'website':webLink, 'gMap':mapLink})
