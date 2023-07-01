from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status

from rest_framework import generics
from rest_framework import viewsets

from django.http import HttpResponse
import traceback
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse 


def index(request):
    return render(request,"index.html")
    


def email(request):
    name = ''
    email = ''
    content = ''

    if request.method== "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["content"]


    html_message = loader.render_to_string(
        'email_sender_app/message.html',
        {
           
            'name': name,

           
            'body':content,
           
            'sign': 'By Pramod',
        })
    send_mail(
        'Congratulations!',
        'You are lucky to receive this mail.',
        'pramodkumar5102002@gmail.com',
        [email], 
        html_message=html_message,
        fail_silently=False,
    )
    return render(request,"messagesuccess.html")


