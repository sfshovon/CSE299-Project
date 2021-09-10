from django.shortcuts import render
from oxygen_cylinder.models import Cylinder_Request
from django.conf import settings
from django.core.mail import send_mail
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
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()
database = firebase.database()
# Create your views here.
def view_oxygen_cylinders(request):
    """
        This method is used to display the list of available oxygen cylinders.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the list of oxygen cylinders in a single page.

        :rtype: HttpResponse.
    """ 
    name = []
    image = []
    priceList = []
    pID = []
    litre = []
    brand = []
    timeStamp = database.child("OxygenCylinder").get()
    timeStampList = []
    for i in timeStamp.each():
        timeStampKey = i.key()
        timeStampList.append(timeStampKey)
    for i in timeStampList:
        id = i
        title = database.child("OxygenCylinder").child(i).child("title").get().val() 
        img = database.child("OxygenCylinder").child(i).child("image").get().val() 
        price = database.child("OxygenCylinder").child(i).child("price").get().val() 
        size = database.child("OxygenCylinder").child(i).child("litre").get().val() 
        pBrand = database.child("OxygenCylinder").child(i).child("brand").get().val()    
        pID.append(id) 
        name.append(title) 
        image.append(img) 
        priceList.append(price)  
        litre.append(size)  
        brand.append(pBrand)     
    cylinderList = zip(pID, name, image, priceList, litre, brand)  
    return render(request, 'oxygen_cylinder/view_oxygen_cylinder.html',{"results": cylinderList})

def cylinder_details(request, keyy):
    """
        This method is used to display the details of a specific cylinder.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the specific cylinder information in a page.

        :rtype: HttpResponse.
    """
    pID = keyy
    mask = database.child("OxygenCylinder").child(keyy).child("Oxygen Mask").get().val() 
    cannula = database.child("OxygenCylinder").child(keyy).child("cannula").get().val() 
    description = database.child("OxygenCylinder").child(keyy).child("description").get().val() 
    flowMeter = database.child("OxygenCylinder").child(keyy).child("flowMeter").get().val()
    trolley = database.child("OxygenCylinder").child(keyy).child("trolley").get().val() 
    size = database.child("OxygenCylinder").child(keyy).child("small").get().val() 
    warranty = database.child("OxygenCylinder").child(keyy).child("warranty").get().val() 
    weight = database.child("OxygenCylinder").child(keyy).child("weight").get().val() 
    height = database.child("OxygenCylinder").child(keyy).child("height").get().val() 
    rate = database.child("OxygenCylinder").child(keyy).child("flowrate").get().val() 
    madeIn = database.child("OxygenCylinder").child(keyy).child("from").get().val() 
    title = database.child("OxygenCylinder").child(keyy).child("title").get().val() 
    image = database.child("OxygenCylinder").child(keyy).child("image").get().val() 
    price = database.child("OxygenCylinder").child(keyy).child("price").get().val() 
    size = database.child("OxygenCylinder").child(keyy).child("litre").get().val() 
    pBrand = database.child("OxygenCylinder").child(keyy).child("brand").get().val() 
    refillPrice = database.child("OxygenCylinder").child(keyy).child("refillTk").get().val() 
    return render(request, 'oxygen_cylinder/cylinder_details.html', {'pID':pID, 'warranty':warranty,'weight':weight,'height':height,'rate':rate,'madeIn':madeIn,'refillPrice':refillPrice,'mask':mask, 'cannula':cannula, 'description':description, 'flowMeter':flowMeter, 'trolley':trolley, 'name':title, 'image':image, 'price':price, 'size':size, 'brand':pBrand})

def request_form(request, keyy):
    """
        This method is used to display the oxygen request form.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page. It returns the form for inserting relevant recipient information.

        :rtype: HttpResponse.
    """
    pID = keyy
    request.session['ID'] = pID
    title = database.child("OxygenCylinder").child(pID).child("title").get().val() 

    return render(request, 'oxygen_cylinder/request_form.html', {'title': title, 'pID':pID})

def oxygen_request(request):
    """
        This method is used to retrieve the relevant user inserted value from the request for oxygen cylinder form.

        It stores the retrieved data in the database.

        It sends an email confirmation about receiving of the request form.

        :param request: It is a HttpResponse from user.

        :type request: HttpResponse.

        :return: This method returns a html page which displays the request received confirmation message.

        :rtype: HttpResponse.
    """
    import time
    import pytz
    tz = pytz.timezone('Asia/Dhaka')
    timeNow = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(timeNow.timetuple()))
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    pID = request.session['ID']
    pName = database.child("OxygenCylinder").child(pID).child("title").get().val()
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    contactNum = request.POST.get('contact')
    address = request.POST.get('address')
    city = request.POST.get('city')
    postalCode = request.POST.get('zip')
    print(firstName, lastName, contactNum, address, city, postalCode, pID)
    data = { 'pID':pID,'pName':pName,
            'firstName':firstName, 'lastName':lastName,
            'contactNum':contactNum,'address':address,
            'city':city, 'postalCode':postalCode
     }
    database.child("Cylinder_Request").child(millis).set(data)
    fName = database.child("Users").child(a).child("fname").get().val()
    lName = database.child("Users").child(a).child("lname").get().val()
    name =fName + " " +lName 
    email = database.child("Users").child(a).child("email").get().val()
    subject = 'Oxygen Cylinder Request'
    message = 'Hello {}. Team Pashe Achi has received your request for purchasing {}. Our customer support team will reach out to you shortly to answer to your request. Thank you.'.format(name, pName)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail(subject, message, email_from, recipient_list)
    return render (request, 'oxygen_cylinder/confirmation.html', {'name':name})
