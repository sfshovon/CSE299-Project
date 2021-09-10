from django.shortcuts import render,redirect
from login_register.models import UserSignUp
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import auth
import pyrebase
import os

"""
Global Variables
"""
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

#ViewProfile
def view_profile(request):    
    """
    This view_profile method is used to retrieve information from database to display
    user profile.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If a user is logged in, it returns a HTML page that displays user profile.

    :rtype: HttpResponse.
    """
    try:
        idToken = request.session['LoginId']
        a = authe.get_account_info(idToken)
        a = a['users']
        a = a[0]
        a = a['localId']
        
        pp = database.child("Users").child(a).child("propic").get().val()
        if (pp==0):
            photolink = 0
        else:
            photolink = pp
        
        userFname = database.child("Users").child(a).child("fname").get().val()
        userLname = database.child("Users").child(a).child("lname").get().val()
        userAge = database.child("Users").child(a).child("age").get().val()
        userDob = database.child("Users").child(a).child("dob").get().val()
        userGender = database.child("Users").child(a).child("gender").get().val()
        userOccupation = database.child("Users").child(a).child("occupation").get().val()
        userCnumber = database.child("Users").child(a).child("cnumber").get().val()
        userBgroup = database.child("Users").child(a).child("bgroup").get().val()
        userEmail = database.child("Users").child(a).child("email").get().val()
        return render(request, 'view_profile/user_profile.html', {'fname':userFname,'lname':userLname,'age':userAge,'dob':userDob,'gender':userGender,'occupation':userOccupation,'cnumber':userCnumber,'bgroup':userBgroup,'email':userEmail, 'photolink':photolink})
  
    except:
        return render(request, 'login_register/landing.html')

  
#DeleteProfileInformation
def delete_profile_information(request):
    """
    This delete_profile_information method is used to delete the users information from database.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If a user is logged in, it will remove the user's information.

    :rtype: HttpResponse.
    """
    idToken = request.session['LoginId']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']
    userId = database.child("Users").get()
    userIdList = []
    for i in userId.each():
        userKey = i.key()
        userIdList.append(userKey)
    
    for i in userIdList:
        if(i==a):
            if request.method == 'POST':
                userFname = database.child("Users").child(a).child("fname").get().val()
                userLname = database.child("Users").child(a).child("lname").get().val()
                userAge = database.child("Users").child(a).child("age").get().val()
                userDob = database.child("Users").child(a).child("dob").get().val()
                userGender = database.child("Users").child(a).child("gender").get().val()
                userOccupation = database.child("Users").child(a).child("occupation").get().val()
                userCnumber = database.child("Users").child(a).child("cnumber").get().val()
                userBgroup = database.child("Users").child(a).child("bgroup").get().val()
                userEmail = database.child("Users").child(a).child("email").get().val()
                pp = database.child("Users").child(a).child("propic").get().val()

                database.child("Users").child(a).remove()
                subject = 'PasheAchi Account Information Deletion'
                message = 'Hello {}, Your PasheAchi account informations have been deleted.'.format(userFname)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [userEmail]
                send_mail(subject, message, email_from, recipient_list)
                return render(request, 'login_register/landing.html')
    return render(request, 'view_profile/user_profile.html')

def update_profile(request):
    """
    This update_profile method is used to show the users information from the database.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If a user is logged in, it returns an update profile page which is HTML a page that shows user information to edit in the database.

    :rtype: HttpResponse.
    """
    userFname = request.POST.get('fname')
    userLname = request.POST.get('lname')
    userAge = request.POST.get('age')
    userDob = request.POST.get('dob')
    userGender = request.POST.get('gender')
    userOccupation = request.POST.get('occupation')
    userCnumber = request.POST.get('cnumber')
    userBgroup = request.POST.get('bgroup')
    

    idToken = request.session['LoginId']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']
    
    data = {"fname":userFname, "lname":userLname, 
            "age":userAge, "dob":userDob, 
            "gender":userGender, "occupation":userOccupation, 
            "cnumber":userCnumber, "bgroup":userBgroup
           
    }

    check = database.child("Users").child(a).update(data)
    if check is not None:
        return redirect("VP")
    else:
        return redirect("VP")

def update_img_url(request):
    """
    This update_img_url method is used to update user image to the database from user's profile.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If a user is logged in, it returns a view profile page which is a HTML page that displays user profile with updated image.

    :rtype: HttpResponse.
    """
    photolink=request.POST['photolink']
    imginfo = {'propic':photolink}
    idToken = request.session['LoginId']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']

    check= database.child("Users").child(a).update(imginfo)
    if check is not None:
        return redirect("VP")
    else:
        return redirect("VP")
        
def edit_profile(request):
    """
    This edit_profile method is used to update the users information into the database.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If a user is logged in, it returns a view profile page which is HTML a page that shows user updated information.

    :rtype: HttpResponse.
    """
    idToken = request.session['LoginId']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']
   
    pp = database.child("Users").child(a).child("propic").get().val()
    if (pp==0):
        photolink = 0
    else:
        photolink = pp
    
    userFname = database.child("Users").child(a).child("fname").get().val()
    userLname = database.child("Users").child(a).child("lname").get().val()
    userAge = database.child("Users").child(a).child("age").get().val()
    userDob = database.child("Users").child(a).child("dob").get().val()
    userGender = database.child("Users").child(a).child("gender").get().val()
    userOccupation = database.child("Users").child(a).child("occupation").get().val()
    userCnumber = database.child("Users").child(a).child("cnumber").get().val()
    userBgroup = database.child("Users").child(a).child("bgroup").get().val()
    userEmail = database.child("Users").child(a).child("email").get().val()

    return render(request, 'view_profile/edit_profile.html', {'fname':userFname,'lname':userLname,'age':userAge,'dob':userDob,'gender':userGender,'occupation':userOccupation,'cnumber':userCnumber,'bgroup':userBgroup,'email':userEmail, 'photolink':photolink})
  