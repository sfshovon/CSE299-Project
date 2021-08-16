from django.shortcuts import render
from make_appointment.models import Appointment
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

"""
Global Variables
"""
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
storage = firebase.storage()
database = firebase.database()

def appointments(request):
    """
    This method is used to retrieve appointments details from database to display patients upcoming appointments.

    :param request: It's a HttpResponse from user.

    :type request: HttpResponse.

    :return: If the database doesn't contain any appointments, it returns a HTML page showing text.
             Else,
                If the user has appointments, it returns a HTML page that displays users upcoming appointments.
                If the user has no appointments, it returns a HTML page showing text.
                
    :rtype: HttpResponse.
    """
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    timeStamp = database.child("Appointments").get()
    if timeStamp is None:
        return render(request, 'viewAppointment/noAppointment.html')
    else:
        timeStampList = []
        for i in timeStamp.each():
            timeStampKey = i.key()
            timeStampList.append(timeStampKey)
        doctorNameList = []
        addressList = []
        appointmentDateList = []
        appointmentTimeList = []
        appointmentIdList = []     
        patientIdView = None
        for i in timeStampList:           
            patientId = database.child("Appointments").child(i).child("patientId").get().val()
            if (patientId == a):
                patientIdView = database.child("Appointments").child(i).child("patientId").get().val()
                tempDate = database.child("Appointments").child(i).child("date").get().val()
                t = tempDate.replace("-","")
                datetimeobject = datetime.strptime(t,'%Y%m%d')
                appDate = datetimeobject.strftime('%d %b %Y')
                appointmentDateList.append(appDate)
                tempTime = database.child("Appointments").child(i).child("timeSlot").get().val()
                appointmentTimeList.append(tempTime)
                doctorId = database.child("Appointments").child(i).child("doctorId").get().val()
                tempDoctorFName = database.child("Doctor").child(doctorId).child("docFName").get().val()
                tempDoctorLName = database.child("Doctor").child(doctorId).child("docLName").get().val()
                doctorFullName = "{} {}".format(tempDoctorFName,tempDoctorLName)
                doctorNameList.append(doctorFullName)            
                tempAddress = database.child("Doctor").child(doctorId).child("docWorkingPlace").get().val()
                addressList.append(tempAddress)
                appointmentId = i
                appointmentIdList.append(appointmentId)
        appointmentDetails = zip(appointmentIdList,addressList,doctorNameList,appointmentDateList,appointmentTimeList)
        if (patientIdView == a):
            patientName = database.child("Users").child(a).child("fname").get().val()
            return render(request, 'viewAppointment/viewAppointment.html',
                        {'appointmentDetails':appointmentDetails,
                        'patientName':patientName,'appointmentIdList':appointmentIdList,})
        else:
            return render(request, 'viewAppointment/noAppointment.html')      

def cancel_appointment(request,appointmentIdList):
    """
    This method is used to cancel appointments and send email after cancellation.

    :param request: It's a HttpResponse from user.
    :param timeStampList: It's the appointment id clicked by user to cancel appointment.

    :type request: HttpResponse.
    :type timeStampList: Integer.

    :return: It returns the HTML page of homepage.

    :rtype: HttpResponse.
    """
    patientId = database.child("Appointments").child(appointmentIdList).child("patientId").get().val()
    doctorId = database.child("Appointments").child(appointmentIdList).child("doctorId").get().val()
    appointmentDate = database.child("Appointments").child(appointmentIdList).child("date").get().val()
    appointmentTime = database.child("Appointments").child(appointmentIdList).child("timeSlot").get().val()
    doctorFName = database.child("Doctor").child(doctorId).child("docFName").get().val()
    doctorLName = database.child("Doctor").child(doctorId).child("docLName").get().val()
    doctorName = doctorFName +" "+ doctorLName
    patientName = database.child("Users").child(patientId).child("fname").get().val()
    doctorEmail = database.child("Doctor").child(doctorId).child("docEmail").get().val()
    if request.method == 'POST':
        database.child("Appointments").child(appointmentIdList).remove()
    subject = 'Pashe Achi Appointment Cancellation'
    message = 'Hello {}, Your appointment on {} at {} with {} has been cancelled.'.format(doctorName,appointmentDate,appointmentTime,patientName)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [doctorEmail,]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'viewAppointment/cancelAppointment.html')