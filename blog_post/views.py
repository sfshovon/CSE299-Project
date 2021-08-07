from django.shortcuts import render, redirect
from blog_post.models import BlogPost
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


def add_post(request):
    """
    This method saves user posts.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: This method redirects to another method "home_page".

    :rtype: HttpResponse.
    """ 
    import time
    import pytz
    tz = pytz.timezone('Asia/Dhaka')
    timeNow = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(timeNow.timetuple()))
    post = request.POST.get('post')
    url = request.POST.get('url')
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    if url == "":
        url = 0
    userFname = database.child("Users").child(a).child("fname").get().val()
    userLname = database.child("Users").child(a).child("lname").get().val()
    userFullName = userFname +" "+ userLname
    data = {
        'userId': a,
        'post': post,
        'fullName': userFullName,
        'comments': 0,
        'likes':0,
        'url':url
    }
    database.child("Blog Post").child(millis).set(data)
    return redirect ("home_page")
    
def home_page(request):
    """
    This method is for blog post home page.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: This method renders a template.

    :rtype: HttpResponse.
    """ 
    import datetime
    timeStamp = database.child("Blog Post").get().val()
    if timeStamp == 0:
        return render(request, 'blog_post/homePage.html')
    else:
        timeStamp = database.child("Blog Post").get()
        timeStampList = []
        for i in timeStamp.each():
            timeStampKey = i.key()
            timeStampList.append(timeStampKey)
        postList = []
        userNameList = []
        dateTimeList = []
        totalLikesList = []
        totalCommentsList = []
        urlList = []
        for i in timeStampList:
            t = float(i)
            dateTime = datetime.datetime.fromtimestamp(t).strftime('%I:%M %p %d-%m-%Y')
            dateTimeList.append(dateTime)
            userName = database.child("Blog Post").child(i).child("fullName").get().val()
            userNameList.append(userName)
            post = database.child("Blog Post").child(i).child("post").get().val()
            postList.append(post)
            url = database.child("Blog Post").child(i).child("url").get().val()
            urlList.append(url)
            totalLikes = 0
            likeCount = database.child("Blog Post").child(i).child("likes").get().val()
            if (likeCount != 0):
                likeCount = database.child("Blog Post").child(i).child("likes").get()
                for j in likeCount.each():
                    totalLikes = totalLikes+1
                totalLikesList.append(totalLikes)
            else:
                totalLikes = 0
                totalLikesList.append(totalLikes)  
            totalComments = 0
            commentCount = database.child("Blog Post").child(i).child("comments").get().val()
            if (commentCount != 0):
                commentCount = database.child("Blog Post").child(i).child("comments").get()
                for j in commentCount.each():
                    totalComments = totalComments+1
                totalCommentsList.append(totalComments)
            else:
                totalComments = 0
                totalCommentsList.append(totalComments)
        postDetails = zip(timeStampList,userNameList,dateTimeList,
                          postList,totalLikesList,totalCommentsList,urlList)
        return render(request, 'blog_post/homePage.html', {'postDetails':postDetails} )

def post_details(request,timeStampList):
    """
    This method is for showing post details of a specific post clicked by an user.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.
    :type timeStampList: Integer.

    :return: This method return a HTML page of post details along with some dictionary values.

    :rtype: HttpResponse.
    """ 
    import datetime
    t = float(timeStampList)
    dateTime = datetime.datetime.fromtimestamp(timeStampList).strftime('%I:%M %p %d-%m-%Y')
    userName = database.child("Blog Post").child(timeStampList).child("fullName").get().val()
    post = database.child("Blog Post").child(timeStampList).child("post").get().val()
    url = database.child("Blog Post").child(timeStampList).child("url").get().val()
    totalLikes = 0
    likeCount = database.child("Blog Post").child(timeStampList).child("likes").get().val()
    if (likeCount != 0):
        likeCount = database.child("Blog Post").child(timeStampList).child("likes").get()
        for j in likeCount.each():
            totalLikes = totalLikes+1
    else:
        totalLikes = 0
    totalComments = 0
    commentTimeStamp = database.child("Blog Post").child(timeStampList).child("comments").get().val()
    if (commentTimeStamp == 0):
        totalComments = 0
        return render(request, 'blog_post/post_details.html',{'dateTime': dateTime,'userName':userName, 'url': url,
                     'post':post,'timeStampList':timeStampList,'totalLikes':totalLikes,'totalComments':totalComments})
    else:
        totalCommentsList = []
        commentTimeStampList = []
        commentTimeStamp = database.child("Blog Post").child(timeStampList).child("comments").get()
        for i in commentTimeStamp.each():
            commentTimeStampKey = i.key()
            commentTimeStampList.append(commentTimeStampKey)
            totalComments = totalComments+1
            totalCommentsList.append(totalComments)
        commentList = []
        commenterList = []
        commentDateTimeList = []
        for i in commentTimeStampList:
            t = float(i)
            commentDateTime = datetime.datetime.fromtimestamp(t).strftime('%I:%M %p %d-%m-%Y')
            commentDateTimeList.append(commentDateTime)
            commenter = database.child("Blog Post").child(timeStampList).child("comments").child(i).child("fullName").get().val()
            commenterList.append(commenter)
            comment = database.child("Blog Post").child(timeStampList).child("comments").child(i).child("comment").get().val()
            commentList.append(comment)
        commentDetails = zip(commentDateTimeList,commenterList,commentList)
        return render(request, 'blog_post/post_details.html',{'commentDetails':commentDetails,'dateTime': dateTime, 'url': url,
                     'userName':userName,'post':post,'timeStampList':timeStampList,'totalLikes':totalLikes,'totalComments':totalComments})

def comment(request,timeStampList):
    """
    This method is to add comments in a post & to save details about comments.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.
    :type timeStampList: Integer.

    :return: This method returns to another method "post_details" and post id.

    :rtype: HttpResponse.
    """ 
    import time
    import pytz
    tz = pytz.timezone('Asia/Dhaka')
    timeNow = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(timeNow.timetuple()))
    comment = request.POST.get('comment')
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    userFname = database.child("Users").child(a).child("fname").get().val()
    userLname = database.child("Users").child(a).child("lname").get().val()
    userFullName = userFname +" "+ userLname
    data = {
        'userId': a,
        'comment': comment,
        'fullName': userFullName
    }
    database.child("Blog Post").child(timeStampList).child("comments").child(millis).set(data)
    return redirect("post_details",timeStampList)

def like(request,timeStampList):
    """
    This method is to add likes in a post & to save details about likes.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.
    :type timeStampList: Integer.

    :return: This method returns to another method "post_details" and post id.

    :rtype: HttpResponse.
    """ 
    import time
    import pytz
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    tz = pytz.timezone('Asia/Dhaka')
    timeNow = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(timeNow.timetuple()))
    like = request.POST.get('next')
    likeCount = database.child("Blog Post").child(timeStampList).child("likes").get().val()
    if (likeCount != 0):
        likeCountList = []
        likeCount = database.child("Blog Post").child(timeStampList).child("likes").get()
        for i in likeCount.each():
            likeCountKey = i.key()
            likeCountList.append(likeCountKey)
        for i in likeCountList:
            total = len(likeCountList)
            if(likeCountKey == a and total == 1):
                database.child("Blog Post").child(timeStampList).child("likes").set(0)
                break
            elif(likeCountKey == a):
                database.child("Blog Post").child(timeStampList).child("likes").child(a).remove()
                break
            else:
                data = {
                    'time': millis
                }
                database.child("Blog Post").child(timeStampList).child("likes").child(a).set(data)
                break
    else:
        data = {
            'time': millis
        }
        database.child("Blog Post").child(timeStampList).child("likes").child(a).set(data)
    return redirect("post_details", timeStampList)

def timeline(request):
    
    idtoken= request.session['LoginId']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    import datetime
    timeStamp = database.child("Blog Post").get().val()
    if timeStamp == 0:
        return render(request, 'blog_post/homePage.html')
    else:
        timeStamp = database.child("Blog Post").get()
        timeStampList = []
        for i in timeStamp.each():
            timeStampKey = i.key()
            timeStampList.append(timeStampKey)
        postList = []
        userNameList = []
        dateTimeList = []
        totalLikesList = []
        totalCommentsList = []
        urlList = []
        for i in timeStampList:
            userId = database.child("Blog Post").child(i).child("userId").get().val()
            if (a != userId):
                continue
            else:
                t = float(i)
                dateTime = datetime.datetime.fromtimestamp(t).strftime('%I:%M %p %d-%m-%Y')
                dateTimeList.append(dateTime)
                userName = database.child("Blog Post").child(i).child("fullName").get().val()
                userNameList.append(userName)
                post = database.child("Blog Post").child(i).child("post").get().val()
                postList.append(post)
                url = database.child("Blog Post").child(i).child("url").get().val()
                urlList.append(url)
                totalLikes = 0
                likeCount = database.child("Blog Post").child(i).child("likes").get().val()
                if (likeCount != 0):
                    likeCount = database.child("Blog Post").child(i).child("likes").get()
                    for j in likeCount.each():
                        totalLikes = totalLikes+1
                    totalLikesList.append(totalLikes)
                else:
                    totalLikes = 0
                    totalLikesList.append(totalLikes)  
                totalComments = 0
                commentCount = database.child("Blog Post").child(i).child("comments").get().val()
                if (commentCount != 0):
                    commentCount = database.child("Blog Post").child(i).child("comments").get()
                    for j in commentCount.each():
                        totalComments = totalComments+1
                    totalCommentsList.append(totalComments)
                else:
                    totalComments = 0
                    totalCommentsList.append(totalComments)
                postDetails = zip(timeStampList,userNameList,dateTimeList,
                          postList,totalLikesList,totalCommentsList,urlList)
    return render(request, 'blog_post/timeline.html', {'postDetails':postDetails} )

def delete_post(request,timeStampList):
    """
    This method is used to delete posts of an user.

    :param request: It's a HttpResponse from user.
    :param timeStampList: It's the post id clicked by user to delete the post.

    :type request: HttpResponse.
    :type timeStampList: Integer.

    :return: It redirects to the timeline of the user.

    :rtype: HttpResponse.
    """
    database.child("Blog Post").child(timeStampList).remove()
    return redirect("timeline")