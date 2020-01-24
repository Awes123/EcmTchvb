from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from .models import Account_detail, Account_User_ID
from random import randint
from django.contrib import messages
# Create your views here.

def login(request):
    pwd="" 
    user=""
    if request.method=="GET":
        if 'username' and 'password' in request.COOKIES:
            user= request.COOKIES['username']
            pwd= request.COOKIES['password']
    elif request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        remember = request.POST.get('rem')
        User=auth.authenticate(username=username,password=password)
        if User is not None:
            if remember:
                user = request.POST.get('username')
                pwd = request.POST.get('password')
                response= render(request,'login/login.html',{'username':user,'password':pwd})
                response.set_cookie('username',user)
                response.set_cookie('password',pwd)
            auth.login(request,User)
            current_user = request.user
            account={}
            if Account_User_ID.objects.filter(user_id=current_user.id).exists():
                acc_Cre=Account_User_ID.objects.get(user_id=current_user.id)
                if acc_Cre.role=="Admin":
                    return redirect('/Management/')
                else:
                    return redirect('/shop/')
        else:
            messages.info(request,'Invalid Credential')
    return render(request, 'login/login.html',{'username':user,'password':pwd})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def sendemail(Subject,text_content,email,html_content):
    print(email)
    from_email=settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(Subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def verifyemail(request):
    retn=""
    if request.method=="POST":
        email=request.POST.get('email','')
        name=request.POST.get('name','')
        if Account_detail.objects.filter(email=email).exists():
            retn="Email is taken"
        else:
            mes= random_with_N_digits(4)
            retn=mes
            Subject = 'NLFC user registration OTP'
            text_content= 'Hi '+name+','
            html_content= '<h4>Hi '+name+',</h4><br> Your OTP for registration in NLFC is : <h5>'+str(mes) +'</h5><br><br> Kindly Use it before page reloading.<br><br><br><b>Best Regards</b><br><b>NLFC Team</b>'
            sendemail(Subject,text_content,email,html_content)
        return HttpResponse(str(retn))

def register(request):
    thank = False
    if request.method=="POST":
        contact_person = request.POST.get('ContactPerson','')
        email = request.POST.get('Email','')
        mobile = request.POST.get('Mobile','')
        Houseno = request.POST.get('Houseno','')
        Colony = request.POST.get('Colony','')
        City=request.POST.get('City','')
        account_detail=Account_detail(contact_person=contact_person,email=email,mobile=mobile,Houseno=Houseno,city=City,Colony=Colony)
        account_detail.save()
        mes= random_with_N_digits(6)
        mes = 'Lucky'+ str(mes)
        user= User.objects.create_user(username=email,first_name=contact_person,email=email,password=mes)
        user.save()
        ac_user=Account_User_ID(account_id=account_detail.account_id,user_id=user.id)
        ac_user.save()
        Subject = 'Lucky Store Credentials'
        text_content= 'Hi '+contact_person+','
        html_content= '<h4>Hi '+contact_person+',</h4><br>Thanks for register on Lucky your credentials: <br><br><b>Username : '+user.username +'</b><br><b>Password : '+mes +'</b><br><b>Best Regards</b><br><b>Lucky Store Team</b>'
        sendemail(Subject,text_content,email,html_content)
        thank = True
    return render(request, 'login/register.html',{'thank':thank})

def reset_password(request):
    messages.info(request,'')
    if request.method=='POST':
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            mes= random_with_N_digits(6)
            mes = 'NLFC'+ str(mes)
            user= User.objects.get(email=email)
            user.set_password(mes)
            user.save()
            Subject = 'NLFC Credentials'
            text_content= 'Hi '+user.first_name+','
            html_content= '<h4>Hi '+user.first_name+',</h4><br>Your new NLFC credentials: <br><br><b>Username : '+user.username +'</b><br><b>Password : '+mes +'</b><br><b>Best Regards</b><br><b>NLFC Team</b>'
            sendemail(Subject,text_content,email,html_content)
            messages.info(request,'We have sent new password on your email.')
            return render(request,'login/login.html')
        else:
            messages.info(request,'Sorry we are unable to find account with this email...!')
    return render(request,'login/reset.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login/login.html')