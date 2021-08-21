from typing import Sized
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

def view_oxygen_cylinders(request):
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
    return render(request, 'oxygen_cylinder/cylinder_details.html', {'warranty':warranty,'weight':weight,'height':height,'rate':rate,'madeIn':madeIn,'refillPrice':refillPrice,'mask':mask, 'cannula':cannula, 'description':description, 'flowMeter':flowMeter, 'trolley':trolley, 'name':title, 'image':image, 'price':price, 'size':size, 'brand':pBrand})

