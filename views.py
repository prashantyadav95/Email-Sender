# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method =="POST" or request.method =="GET":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub,msg,email)
    send_mail(
        sub,msg,'prashant.12band@gmail.com',[email]
             )
    return HttpResponse("Email Sent")
    return render(request,'sender/form.html')