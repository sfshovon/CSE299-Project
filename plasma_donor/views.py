from django.shortcuts import render,redirect
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
    donorReport = database.child("Users").child(a).child("donor").get().val()
    if (donorReport == "Yes"):
        userFname = database.child("Users").child(a).child("fname").get().val()
        return render(request, 'plasma_donor/alreadyDonor.html',{'userFname':userFname})
    else:
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
    tempAge = int(age)
    if (negativeAns == "Yes" and tempWeight>=50 and tempAge>=18 and tempAge<=65):
        database.child("Users").child(a).update({"weight": weight})
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
    data = {
        'experience':experience,
        'covidReportUrl':covidReportUrl,
        'positiveDate':positiveDate,
        'negativeDate':negativeDate,
    }
    database.child("Users").child(a).update({"bgroup": bloodGroup})
    database.child("Users").child(a).update({"district": district})
    database.child("Users").child(a).update({"donor": "Yes"})
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

def donor_list(request):
    return render(request, 'plasma_donor/viewDonors.html')

def a_positive(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("A+").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("A+").get()
        bloodGroup = "A+"
        return redirect('donor_details')

def a_negative(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("A-").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("A-").get()
        bloodGroup = "A-"
        return redirect('donor_details')

def b_positive(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("B+").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("B+").get()
        bloodGroup = "B+"
        return redirect('donor_details')

def b_negative(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("B-").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("B-").get()
        bloodGroup = "B-"
        return redirect('donor_details')

def ab_positive(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("AB+").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("AB+").get()
        bloodGroup = "AB+"
        return redirect('donor_details')

def ab_negative(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("AB-").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("AB-").get()
        bloodGroup = "AB-"
        return redirect('donor_details')

def o_positive(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("O+").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("O+").get()
        bloodGroup = "O+"
        return redirect('donor_details')

def o_negative(request):
    global donors, bloodGroup
    donors = database.child("Plasma Donors").child("O-").get().val()
    if donors == None:
        return render(request, 'plasma_donor/noDonor.html')
    else:
        donors = database.child("Plasma Donors").child("O-").get()
        bloodGroup = "O-"
        return redirect('donor_details')

def donor_details(request):
    donorList = []
    for i in donors.each():
        donorKey = i.key()
        donorList.append(donorKey)
    nameList = []
    ageList = []
    emailList = []
    contactList = []
    genderList = []
    occupationList = []
    proPicList = []
    districtList = []
    for i in donorList:
        fname = database.child("Users").child(i).child("fname").get().val()
        lname = database.child("Users").child(i).child("lname").get().val()
        fullName = fname +" "+ lname
        nameList.append(fullName)
        age = database.child("Users").child(i).child("age").get().val()
        ageList.append(age)
        email = database.child("Users").child(i).child("email").get().val()
        emailList.append(email)
        gender = database.child("Users").child(i).child("gender").get().val()
        genderList.append(gender)
        occupation = database.child("Users").child(i).child("occupation").get().val()
        occupationList.append(occupation)
        contact = database.child("Users").child(i).child("cnumber").get().val()
        contactList.append(contact)
        district = database.child("Users").child(i).child("district").get().val()
        districtList.append(district)
        proPic = database.child("Users").child(i).child("propic").get().val()
        proPicList.append(proPic)
    donorDetails = zip(nameList,ageList,emailList,genderList,occupationList,contactList,proPicList,districtList)
    return render(request, 'plasma_donor/donorList.html',{'donorDetails':donorDetails, 'bloodGroup':bloodGroup})