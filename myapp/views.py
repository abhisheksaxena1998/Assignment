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
            "malware" : False,
            "datetime" : str(datetime.datetime.now())
        }
    response = JsonResponse(mydict)
    return response  

def timeinfo(request):
    text=request.GET['query']
    test = Url.objects.get(time=text)
    print (test.uid)
    mydict = {
            "unique_id" : test.pno,
            "index" : test.index,
            "name" : test.name,
            "result" : test.result,
            "time" : test.time,
            "phone number" : test.pno,
            "created_at" :test.created_at
        }
    response = JsonResponse(mydict)
    return response      

def updatetime(request):
    text=request.GET['oldtime']
    text2=request.GET['newtime']
    test = Url.objects.get(time=text)
    print (test.uid)

    test.time=text2
    test.save(update_fields=['time'])
    test = Url.objects.get(time=text2)

    mydict = {
            "unique_id" : test.pno,
            "index" : test.index,
            "name" : test.name,
            "result" : test.result,
            "time" : test.time,
            "phone number" : test.pno,
            "created_at" :test.created_at
        }
    response = JsonResponse(mydict)
    return response       

def ticketinfo(request):
    text=request.GET['query']
    test = Url.objects.get(uid=text)
    print (test.uid)
    mydict = {
            "unique_id" : test.pno,
            "index" : test.index,
            "name" : test.name,
            "result" : test.result,
            "time" : test.time,
            "phone number" : test.pno,
            "created_at" :test.created_at
        }
    response = JsonResponse(mydict)
    return response  


def deleteticket(request):
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

# Create your views here.

def automated_testing(request):
    
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
                obj.uid = text
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
import joblib
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
import pickle
import socket
import geocoder
import whois
import datetime


def result(request):
    text=request.GET['nm'].strip()

    result="booked"
    uid=request.GET['uniqueid'].lower().strip()
    pno=request.GET['phonenumber'].lower().strip()
    time=request.GET['time'].lower().strip()
    name=text
    #bookedat=str(datetime.datetime.now())
    obj = Url()
    obj.result = result            
    tags = [text,uid,pno,time]
    tags = list(filter(lambda x: x!="Not Found",tags))
    tags.append(text)
    obj.uid = text
    obj.pno = pno
    obj.time = time
    obj.name=name
    #obj.bookedat=str(datetime.datetime.now())    
    obj.save()
    return geturlhistory(request)




def api(request):
    text=request.GET['query'].lower().strip()
    try:
        
        import datetime

        if text.startswith('https://mudvfinalradar.eu-gb.cf.appdomain.cloud/'):
            import datetime
            mydict = {
                "query" : text,
                "malware" : False,
                "datetime" : str(datetime.datetime.now())
            }
            response = JsonResponse(mydict)
            return response   

        if text.startswith('https://www.google.com/search?q='):
            import datetime
            mydict = {
                "query" : text,
                "malware" : False,
                "datetime" : str(datetime.datetime.now())
            }
            response = JsonResponse(mydict)
            return response    


        #if (text.startswith('https://www.google.com/search?q=')==False) :

        else:
        
            if text.startswith('https://') or text.startswith('http://'):
                import tldextract
                do=tldextract.extract(text).domain
                sdo=tldextract.extract(text).subdomain
                suf=tldextract.extract(text).suffix

                if len(text)<=9:
                    return render(request,'errorpage.html')
                aburl=-1
                digits="0123456789"
                if text[8] in digits:
                    oneval=-1
                else:
                    oneval=1    
                if len(text)>170:
                    secval=-1
                else:
                    secval=1  
                if "@" in text:
                    thirdval=-1
                else:
                    thirdval=1    
                k=text.count("//")          
                if k>1:
                    fourthval=-1
                else:
                    fourthval=1
                    
                if "-" in do or "-" in sdo:
                    fifthval=-1
                else:
                    fifthval=1         
                if "https" in text:
                    sixthval=1
                else:
                    sixthval=-1
                temp=text
                temp=temp[6:]
                k1=temp.count("https")

                if k1 >=1:
                    seventhval=-1
                else:
                    seventhval=1
                if "about:blank" in text:
                    eighthval=-1
                else:
                    eighthval=1
                if "mail()" or "mailto:" in text:
                    ninthval=-1
                else:
                    ninthval=1
                re=text.count("//")          
                if re>3:
                    tenthval=-1
                else:
                    tenthval=1    

                import whois
                from datetime import datetime

                url=text

                d=0
                try:
                    res=whois.whois(url)
                except:
                    #print("getaddrerrror DNE")
                    d=-1
                    name="Not found in database"
                    org="Not found in database"
                    add="Not found in database"
                    city="Not found in database"
                    state="Not found in database"
                    ziip="Not found in database"
                    country="Not found in database"
                    emails="Not found in database"
                    dom="Not Found"
                if d!=-1:    
                    try:
                        if len(res.creation_date)>1:
                            a=res['creation_date'][0]
                            b=datetime.now()
                            c=b-a
                            d=c.days
                    except:
                        a=res['creation_date']
                        b=datetime.now()
                        c=b-a
                        d=c.days
                """except:
                    print("getaddrerrror DNE")
                    d=0"""


                

                if d>365:
                    eleventhval=1
                    aburl=1
                elif d<=365:
                    eleventhval=-1
                    aburl=-1
                    var11="Domain age working less than a year"
        
     



                if aburl==-1:
                    twelthval=-1
                else:
                    twelthval=1                 
                import urllib.request, sys, re
                import xmltodict, json
                rank=-1
                try:
                    xml = urllib.request.urlopen('http://data.alexa.com/data?cli=10&dat=s&url={}'.format(text)).read()

                    result= xmltodict.parse(xml)

                    data = json.dumps(result).replace("@","")
                    data_tojson = json.loads(data)
                    url = data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["URL"]
                    rank= int(data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["TEXT"])
                    #print ("rank",rank)
                    if rank<=150000:
                        thirt=1
                    else:
                        thirt=-1
                    #print (thirt)    
                except:
                    thirt=-1 
                    rank=-1
                    #rank="Not Indexed by Alexa"
                    #print (rank)                  




                filename = 'phish_trainedv7mud0.001.sav'

                loaded_model = joblib.load(filename)

                arg=loaded_model.predict(([[oneval,secval,thirdval,fourthval,fifthval,seventhval,eighthval,ninthval,tenthval,eleventhval,twelthval,thirt]]))
                #print (arg[0])
                import whois
                url=text
                
                #print (res)
                if (d!=-1):
                    name=res.domain_name
                    #print (res.domain_name)
                    org=res.org
                    #print (res.org)
                    add=res.address
                    #print (res.address)
                    city=res.city
                    #print (res.city)
                    state=res.state
                    #print (res.state)
                    ziip=res.zipcode
                    #print (res.zipcode)
                    country=res.country
                    #print (res.country)
                    emails=res.emails
                    #print (res.emails)
                    dom=res.domain_name
                    #print (res.domain_name)                
                else:
                    name="Not found in database"
                    org="Not found in database"
                    add="Not found in database"
                    city="Not found in database"
                    state="Not found in database"
                    ziip="Not found in database"
                    country="Not found in database"
                    emails="Not found in database"
                    dom="Not Found"

                
                    

                if aburl==-1 and rank==-1 :
                    arg[0]=-1
                    #phishing

                if arg[0]==1:
                    te="Legitimate"
                else:
                    te="Malicious"  
                if arg[0] == 1:
                    mal = True
                else:
                    mal = False      


                if arg[0] == 1:
                    malstatus = False
                else:
                    malstatus = True                 
                from json.encoder import JSONEncoder
                final_entity = { "predicted_argument": [int(arg[0])]}

            import datetime
            mydict = {
                "query" : url,
                "malware" : malstatus,
                "datetime" : str(datetime.datetime.now())
            }
            response = JsonResponse(mydict)
            return response

                

    except:
        text=request.GET['query']
        import datetime
        mydict = {
            "query" : text,
            "malware" : False,
            "datetime" : str(datetime.datetime.now())
        }
        response = JsonResponse(mydict)
        return response  
        #return render(request,'404.html')       



def testresults(request):
    #return HttpResponse("about")
    return render(request, 'testresults.html')
        

def about(request):
    #return HttpResponse("about")
    try:
        return render(request, 'about.html')
    except:
        return render(request, 'about.html')
    
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
