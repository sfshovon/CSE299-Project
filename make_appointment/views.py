from django.shortcuts import render, redirect
from make_appointment.models import Appointment
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timezone
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

"""
Global Variables
"""
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()
database = firebase.database()

def create_appointment(request):
    """
    This method is used to retrieve doctor's name,id,timeslot from database to display in the appointment form.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: This method redirects to another method.

    :rtype: HttpResponse.
    """ 
    from datetime import datetime
    docId = database.child("Doctor").get()
    docIdList = []
    for i in docId.each():
        docIdKey = i.key()
        docIdList.append(docIdKey)
    doctorNameList = []
    timeOneList = []
    timeTwoList = []
    doctorId = []
    consultationDay = []
    for i in docIdList:
        doctorFName = database.child("Doctor").child(i).child("docFName").get().val()
        doctorLName = database.child("Doctor").child(i).child("docLName").get().val()
        doctorFullName = doctorFName +" "+ doctorLName
        doctorNameList.append(doctorFullName)
        tempTimeOne = database.child("Doctor").child(i).child("docWorkingHour1").get().val()
        d1 = datetime.strptime(tempTimeOne, "%H:%M")
        timeOne = d1.strftime("%I:%M %p")
        timeOneList.append(timeOne)
        tempTimeTwo = database.child("Doctor").child(i).child("docWorkingHour2").get().val()
        d2 = datetime.strptime(tempTimeTwo, "%H:%M")
        timeTwo = d2.strftime("%I:%M %p")
        timeTwoList.append(timeTwo)
        dId = i
        doctorId.append(dId)
        tempConsultationDay = database.child("Doctor").child(i).child("consultationDayValue1").get().val()
        consultationDay.append(tempConsultationDay)
    allDoctorName = zip(doctorNameList,doctorId)
    timeSlot = zip(doctorId,timeOneList,timeTwoList)
    day = zip(doctorId,consultationDay)
    return render(request, 'makeAppointment/makeAppointment.html',
                {'allDoctorName':allDoctorName,'timeSlot':timeSlot, 'day':day})

def appointment_form(request):
    """
    This method is used to get the values from the appointment form to store data of appointments in the database.
    And it sends the confirmation email of appointment to the doctor and patient.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: This method redirects to another method.

    :rtype: HttpResponse.
    """ 
    import time
    import pytz
    tz = pytz.timezone('Asia/Dhaka')
    timeNow = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(timeNow.timetuple()))
    doctorId = request.POST.get('doctorId')
    date = request.POST.get('date')
    timeSlot = request.POST.get('timeSlot')
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    data = {
        'date':date,
        'timeSlot':timeSlot,
        'patientId': a,
        'doctorId':doctorId
    }
    doctorFName = database.child("Doctor").child(doctorId).child("docFName").get().val()
    doctorLName = database.child("Doctor").child(doctorId).child("docLName").get().val()
    doctorFullName = doctorFName +" "+ doctorLName
    doctorEmail = database.child("Doctor").child(doctorId).child("docEmail").get().val()
    patientFName = database.child("Users").child(a).child("fname").get().val()
    patientLName = database.child("Users").child(a).child("lname").get().val()
    patientFullName = patientFName +" "+ patientLName
    patientEmail = database.child("Users").child(a).child("email").get().val()
    # subject = 'Pashe Achi Appointment Confirmation'
    # message = 'Hello {}, Your appointment with {} is confirmed.'.format(patientFullName,doctorFullName)
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [patientEmail,]
    # send_mail(subject, message, email_from, recipient_list)
    # subject = 'Pashe Achi Appointment Confirmation'
    # message = 'Hello {}, {} has added an appointment with you on {} at {}.'.format(doctorFullName,patientFullName,date,timeSlot)
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [doctorEmail,]
    # send_mail(subject, message, email_from, recipient_list)
    database.child("Appointments").child(millis).set(data)
    return render(request, 'makeAppointment/confirm.html', {'patientFullName':patientFullName})