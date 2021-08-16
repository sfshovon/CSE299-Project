from django.shortcuts import render,redirect
from datetime import datetime, timezone
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
"""
Global Variables
"""
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()
database = firebase.database()

def become_donor(request):
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    donorReort = database.child("Users").child(a).child("donor").get().val()
    if (donorReort == "Yes"):
        userFname = database.child("Users").child(a).child("fname").get().val()
        return render(request, 'plasma_donor/alreadyDonor.html',{'userFname':userFname})
    else:
        return render(request, 'plasma_donor/becomeDonor.html')
    return render(request, 'plasma_donor/becomeDonor.html')

def eligibility(request):
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    negativeAns = request.POST.get('negative')
    weight = request.POST.get('weight')
    tempWeight = int(weight)
    age =  database.child("Users").child(a).child("age").get().val()
    if (negativeAns == "Yes" and tempWeight>=50 and age>=18 and age<=65):
        database.child("Users").child(a).update({"weight": weight})
        database.child("Users").child(a).update({"donor": "Yes"})
        districtList =["Dhaka","Faridpur","Gazipur","Gopalganj","Jamalpur","Kishoreganj","Madaripur","Manikganj",
        "Munshiganj","Mymensingh","Narayanganj","Narsingdi","Netrokona","Rajbari","Shariatpur","Sherpur","Tangail",
        "Bogra","Joypurhat","Naogaon","Natore","Nawabganj","Pabna","Rajshahi","Sirajgonj","Dinajpur","Gaibandha",
        "Kurigram","Lalmonirhat","Nilphamari","Panchagarh","Rangpur","Thakurgaon","Barguna","Barisal","Bhola",
        "Jhalokati","Patuakhali","Pirojpur","Bandarban","Brahmanbaria","Chandpur","Chittagong","Comilla","Cox's Bazar",
        "Feni","Khagrachari","Lakshmipur","Noakhali","Rangamati","Habiganj","Maulvibazar","Sunamganj","Sylhet","Bagerhat",
        "Chuadanga","Jessore","Jhenaidah","Khulna","Kushtia","Magura","Meherpur","Narail","Satkhira"]
        districtList.sort()
        return render(request, 'plasma_donor/addDonor.html',{'districtList':districtList})
    else:
        return render(request, 'plasma_donor/notEligible.html')

def add_donor(request):
    bloodGroup = request.POST.get('bloodgroup')
    district = request.POST.get('district')
    positiveDate = request.POST.get('positiveDate')
    negativeDate = request.POST.get('negativeDate')
    experience = request.POST.get('experience')
    covidReportUrl = request.POST.get('url')
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    userFname = database.child("Users").child(a).child("fname").get().val()
    userLname = database.child("Users").child(a).child("lname").get().val()
    userFullName = userFname +" "+ userLname
    userAge = database.child("Users").child(a).child("age").get().val()
    userWeight = database.child("Users").child(a).child("weight").get().val()
    userDob = database.child("Users").child(a).child("dob").get().val()
    userGender = database.child("Users").child(a).child("gender").get().val()
    userOccupation = database.child("Users").child(a).child("occupation").get().val()
    userContactNumber = database.child("Users").child(a).child("cnumber").get().val()
    userEmail = database.child("Users").child(a).child("email").get().val()
    data = {
        'name': userFullName,
        'age': userAge,
        'weight':userWeight,
        'dob': userDob,
        'gender': userGender,
        'district':district,
        'occupation': userOccupation,
        'contactNumber': userContactNumber,
        'email': userEmail,
        'experience':experience,
        'covidReportUrl':covidReportUrl,
        'positiveDate':positiveDate,
        'negativeDate':negativeDate,
    }
    if (bloodGroup == "A+"):
        database.child("Plasma Donors").child("A+").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "A-"):
        database.child("Plasma Donors").child("A-").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "B+"):
        database.child("Plasma Donors").child("B+").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "B-"):
        database.child("Plasma Donors").child("B-").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "AB+"):
        database.child("Plasma Donors").child("AB+").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "AB-"):
        database.child("Plasma Donors").child("AB-").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "O+"):
        database.child("Plasma Donors").child("O+").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    if (bloodGroup == "O-"):
        database.child("Plasma Donors").child("O-").child(a).set(data)
        return render(request, 'plasma_donor/addedDonor.html')
    return render(request, 'plasma_donor/addedDonor.html')