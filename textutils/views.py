# We have created this website

from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    name= 'Raja'
    params={'name':name}
    return render(request,'index.html',params)


def removepunc(request):
    if request.method=='GET':
        sen= request.GET.get('text','default')
        params =ProcessText.removepunc(sen)
        
        return render(request,'removepunc.html',params)
        
    return render(request,'forms/removepunc.html')

def removepuncform(request):
        return render(request,'forms/removepunc.html')

def capfirst(request):
    if request.method=='GET':
        sen= request.GET.get('text','default')
        params =ProcessText.capfirst(sen)
        
        return render(request,'capfirst.html',params)
    return render(request,'forms/capfirst.html')

def capfirstform(request):
        return render(request,'forms/capfirst.html')

def newlineremove(request):
    if request.method=='GET':
        sen= request.GET.get('text','default')
        params =ProcessText.newlineremove(sen)
        
        return render(request,'newlineremove.html',params)

    return render(request,'forms/newlineremove.html')

def newlineremoveform(request):
    return render(request,'forms/newlineremove.html')

def spaceremove(request):
    if request.method=='GET':
        sen= request.GET.get('text','default')
        params =ProcessText.spaceremove(sen)
        
        return render(request,'spaceremove.html',params)

    return render(request,'forms/spaceremove.html')

def spaceremoveform(request):
        return render(request,'forms/spaceremove.html')

def charcount(request):
    
    if request.method=='GET':
        sen= request.GET.get('text','default')
        params =ProcessText.charcount(sen)
        
        return render(request,'charcount.html',params)

    return render(request,'forms/charcount.html')   

def charcountform(request):
    return render(request,'forms/charcount.html') 




class ProcessText:
    def removepunc(sen):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
        for x in sen.lower(): 
            if x in punctuations: 
                sen = sen.replace(x, "")
                        
        params={'sen':sen}
        return params 

    def capfirst(sen):
        s=" "
        s= sen.capitalize()
        params={'sen':s}
        return params 
        

    def charcount(sen):
        l=len(sen)
        params= {'sen':l} 
        return params

    def spaceremove(sen):
        l= len(sen)
        s=" "
        for i in range(l):
            if sen[i]!=' ':
                print(sen[i],)
                s= s+sen[i]
        params= {'sen':s} 
        return params 

    def newlineremove(sen):
        sen= sen.replace("\n","")
        params={'sen':sen}
        return params 


