from datetime import datetime
import random
import uuid
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django_app.models import ConfirmationKey
from bs4 import BeautifulSoup

# Create your views here.


# Load home page
def home(request):
    return render(request, 'index.html')
  

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('emailid')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=emailid):
             messages.error(request, "User already Exists)")
           
        if password1 != password2:
            messages.error(request, "Confirm password did not matched !")
      

        register = User.objects.create_user(username=emailid, email=emailid, password=password1)
        register.first_name = name
        register.save()

        messages.success(request, 'Your account created successfully !')
       
    return render(request, 'registration.html')



def userlogin(request):
    if request.method == "POST":
        emailid = request.POST.get('emailid')
        pass1 = request.POST.get('password')

        user_aut = authenticate(username = emailid, password = pass1)
        if user_aut is not None :
            login(request, user_aut)
            fname= user_aut.first_name
            return render(request, 'index.html', {'fname': fname})
        else:
            messages.error(request, "Bad credentials !")

    return render(request, 'login.html')      


def about(request):
    return render(request, 'about.html')

def userlogout(request):
    logout(request)

    messages.success(request, 'User Logged out successfully !')
    return redirect("/")


def contact(request):
    return render(request, 'contact.html')


def sendlink(request):
    subject = "Welcome to JR Technology Django Email"
    from_email = settings.EMAIL_HOST_USER
    to_email = ["raghu.bhandari.tech@gmail.com"]
    uid= uuid.uuid1(random.randint(0, 281474976710655))
    
  
    # send_mail( subject, message, from_email, to_email )
    DB = ConfirmationKey(key=uid, emailid=to_email[0])
    DB.save()

    message = "You are registered successfully and Your activation key: "+ str(uid)
    messages.success(request, message)

    return render(request, 'registration.html')


def verifyuser(request):

    url_key = request.GET['key']

    if url_key != "":
        obj = ConfirmationKey.objects.filter(key=url_key)
        if obj:
            ConfirmationKey.objects.update(updated_date = datetime.now())
            messages.success(request, url_key)
        else:
            messages.error(request, "Invalid key: "+ url_key)

    return render(request, 'verify.html')



def webscraping(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", {'class': 'chart full-width'})
    rows = table.find_all("tr")
    movies = []


    for row in rows:
        images = row.find('img')
        if images:
            movies.append(images["alt"])
            # movies.append(images["src"])
            # print(images)

    
    print(movies)

    return render(request, 'webscraping.html', {'movies': movies})

    
    

# context = {
#         'variable': "This is server value",
#         'variable2': "Python is Great"
#     }
