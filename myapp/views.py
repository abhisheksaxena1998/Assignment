#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import *

def searchRec(request):
    test = Url.objects.get(name="testname4")
    print (test.uid)
    mydict = {
            "query" : test.pno,
            "m" : False,
            "datetime" : str(datetime.datetime.now())
        }
    response = JsonResponse(mydict)
    return response  

def deleteTime():   # Function to delete all the tickets which are expired automatically.
    now=datetime.datetime.now()
    test = Url.objects.all()
    for i in test:
        text=datetime.datetime.strptime(i.time,'%d/%m/%Y %H:%M:%S')
        if (now-text).total_seconds()//3600>=8:
            todel = Url.objects.get(uid=i.uid)
            todel.delete()
    mydict = {
            "status" : "Record deleted successfully!",
            "time of deletion" : str(datetime.datetime.now())
        }
    response = JsonResponse(mydict)
    return 1

def listall(request):
    deleteTime()    # Function to delete all the tickets which are expired automatically is called in every endpoint for automated deletion 
    text=request.GET['query']
    test = Url.objects.filter(time=text)
    for i in test:
        print (i)
    print (len(test))
    array=[]
    for i in test:
        d = {
            "unique_id" : i.uid,
            "index" : i.index,
            "name" : i.name,
            "result" : i.result,
            "time" : i.time,
            "phone number" : i.pno,
            "created_at" :i.created_at
        }
        array.append(d)

    response = JsonResponse(array,safe=False)
    return response      

def showallrecords(request):
    deleteTime()
    test = Url.objects.all()
    for i in test:
        print (i)
    print (len(test))
    array=[]
    for i in test:
        d = {
            "unique_id" : i.uid,
            "index" : i.index,
            "name" : i.name,
            "result" : i.result,
            "time" : i.time,
            "phone number" : i.pno,
            "created_at" :i.created_at
        }
        array.append(d)

    response = JsonResponse(array,safe=False)
    return response  


def timeinfo(request):
    try:
        deleteTime()
        text=request.GET['query']
        test = Url.objects.get(time=text)
        print (test.uid)
        mydict = {
                "unique_id" : test.uid,
                "index" : test.index,
                "name" : test.name,
                "result" : test.result,
                "time" : test.time,
                "phone number" : test.pno,
                "created_at" :test.created_at
            }
        response = JsonResponse(mydict)
        return response      
    except:
        mydict = {
                "status" : "Matching query does not exist",
                "error code" : 500
            }
        response = JsonResponse(mydict)
        return response      

def updatetime(request):
    try:
        deleteTime()
        text=request.GET['oldtime']
        text2=request.GET['newtime']
        test = Url.objects.get(time=text)
        print (test.uid)

        test.time=text2
        test.save(update_fields=['time'])
        test = Url.objects.get(time=text2)

        mydict = {
                "unique_id" : test.uid,
                "index" : test.index,
                "name" : test.name,
                "result" : test.result,
                "time" : test.time,
                "phone number" : test.pno,
                "created_at" :test.created_at
            }
        response = JsonResponse(mydict)
        return response       
    except:
        mydict = {
                "status" : "Matching query does not exist",
                "error code" : 500
            }
        response = JsonResponse(mydict)
        return response      

def ticketinfo(request):
    try:
        deleteTime()
        text=request.GET['query']
        test = Url.objects.get(uid=text)
        print (test.uid)
        mydict = {
                "unique_id" : test.uid,
                "index" : test.index,
                "name" : test.name,
                "result" : test.result,
                "time" : test.time,
                "phone number" : test.pno,
                "created_at" :test.created_at
            }
        response = JsonResponse(mydict)
        return response  
    except:
        mydict = {
                "status" : "Matching query does not exist",
                "error code" : 500
            }
        response = JsonResponse(mydict)
        return response  



def deleteticket(request):
    try:
        deleteTime()
        text=request.GET['query']
        test = Url.objects.get(uid=text)
        print (test.uid)
        test.delete()
        mydict = {
                "status" : "Record deleted successfully!",
                "time of deletion" : str(datetime.datetime.now())
            }
        response = JsonResponse(mydict)
        return response 
    except:
        mydict = {
                "status" : "Matching query does not exist",
                "error code" : 500
            }
        response = JsonResponse(mydict)
        return response      

# Create your views here.

def automated_testing(request):
    deleteTime()
    import re
    import json
    import requests


    if request.method == "POST":
        uploaded_file = request.FILES['upload_file']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        #f = open("media/"+uploaded_file.name, "r")
        with open("media/"+uploaded_file.name, "r") as f:
            for line in f:
                current = line.split(",")
                obj = Url()
                obj.result = 'booked'   
                text=current[0]
                uid=current[1]
                pno=current[2]
                time=current[3]
                name=current[0] 
                tags = [text,uid,pno,time]
                tags = list(filter(lambda x: x!="Not Found",tags))
                tags.append(text)
                obj.uid = uid
                obj.pno = pno
                obj.time = time
                obj.name=name
                #obj.bookedat=str(datetime.datetime.now())    
                obj.save()

        #print (dis)       
        response = JsonResponse("Record Added",safe=False)
        return (response)




def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')


def getuserfeedbackform(request):
    try:
        return render(request, 'userfeedbackform.html')
    except:
        return render(request, '404.html')


def saveuserfeedbackform(request):
    try:
        obj = UserFeedBack()
        obj.title = request.GET['usertitle']
        obj.description = request.GET['userdescription']
        obj.save()
        mydict = {'feedback': True}
        return render(request, 'userfeedbackform.html', context=mydict)
    except:
        return render(request, '404.html')

import warnings
warnings.warn = warn
import warnings
from lxml import html
from json import dump, loads
from requests import get
import json
from re import sub
from dateutil import parser as dateparser
from time import sleep
from django.http import HttpResponse
from django.shortcuts import render
import os

import socket

import datetime

def addRecord(request):
    deleteTime()
    text=request.GET['nm'].strip()
    result="booked"
    uid=request.GET['uniqueid']
    pno=request.GET['phonenumber']
    time=request.GET['time']
    name=text
    count=0
    test=Url.objects.all()
    for i in test:
        if i.time==time:
            count+=1
    if count<=20:        
        #bookedat=str(datetime.datetime.now())
        obj = Url()
        obj.result = result            
        tags = [text,uid,pno,time]
        tags = list(filter(lambda x: x!="Not Found",tags))
        tags.append(text)
        obj.uid = uid
        obj.pno = pno
        obj.time = time
        obj.name=name
        #obj.bookedat=str(datetime.datetime.now())    
        obj.save()
        mydict = {
            "status" : "Record added successfully!"       
        }
        response = JsonResponse(mydict)
        return response     
        
    else:
        mydict = {
            "status" : "Record can't be added!",
            "error_message" : "Record exceeded '20' limit!"
        }
        response = JsonResponse(mydict)
        return response 



def result(request):
    deleteTime()
    text=request.GET['nm'].strip()

    result="booked"
    uid=request.GET['uniqueid']
    pno=request.GET['phonenumber']
    time=request.GET['time']
    name=text
    #bookedat=str(datetime.datetime.now())
    obj = Url()
    obj.result = result            
    tags = [text,uid,pno,time]
    tags = list(filter(lambda x: x!="Not Found",tags))
    tags.append(text)
    obj.uid = uid
    obj.pno = pno
    obj.time = time
    obj.name=name
    #obj.bookedat=str(datetime.datetime.now())    
    obj.save()
    return geturlhistory(request)
        
    
def geturlhistory(request):
    
    mydict = {
        "urls" : Url.objects.all().order_by('-created_at')
    }
    return render(request,'list.html',context=mydict)
    
def discuss(request):
    try:
        mydict = {
            "users" : UserFeedBack.objects.all()
        }
        return render(request,'discuss.html',context=mydict)
    except:
        return render(request,'404.html')

def search(request):
    try:
        query = request.GET['search']
        query = str(query).lower()
        mydict = {
            "urls" : Url.objects.all().filter(Q(link__contains=query) | Q(result__contains=query) | Q(created_at__contains=query) |
            Q(rank__contains=query) | Q(dom__contains=query)  | Q(country__contains=query) | Q(state__contains=query) | Q(emails__contains=query) |
            Q(add__contains=query) | Q(org__contains=query) | Q(city__contains=query)
            ).order_by('-created_at')
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')

def replyform(request,replyid):
    try:
        obj = UserFeedBack.objects.get(userid=replyid)
        mydict = {
        "replyid" : obj.userid,
        "title" : obj.title,
        "description" : obj.description
        }
        return render(request,'reply.html',context=mydict)
    except:
        return render(request,'404.html')

def savereply(request):
    try:
        #print("debug start")
        replyid = request.GET['replyid']
        #print(replyid)
        obj = UserFeedBack.objects.get(userid=replyid)
        obj.replied = True
        obj.reply = request.GET['userreply']
        obj.save()
        mydict = {
            "reply" : True,
            "users" : UserFeedBack.objects.all()
        }
        #print("debug end")
        return render(request,'discuss.html',context=mydict)

    except:
        return render(request,'404.html')

def searchdiscuss(request):
    try:
        query = request.GET['search']
        query = str(query).lower()
        mydict = {
            "users" : UserFeedBack.objects.all().filter(Q(title__contains=query) | Q(description__contains=query) | Q(created_at__contains=query)
            |  Q(replied__contains=query) | Q(reply__contains=query)
            )
        }
        return render(request,'discuss.html',context=mydict)
    except:
        return render(request,'404.html')
