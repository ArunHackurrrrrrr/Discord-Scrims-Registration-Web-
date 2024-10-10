#THIS FILE IS CREATED BY ME - ARUN
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # GET THE TEXT USER ENTERED ON THE WEBSITE
    removePunc = request.POST.get('remove pucuation','off')
    fullCaps = request.POST.get('Capitalizer','off')
    newLine = request.POST.get('New line remove','off')
    spaceReamove = request.POST.get('Space remover','off')
    if removePunc =='on':
        # djtext=request.GET.get('text', 'default') dekho .GET.get se bhi kaam hojaata hai par .GET hamesha data url se bhejta hai and there is an limit of sending data over url and url dikhta bhi hai so personal info khatre me hoti hai so insted of .GET  we will use .post to get our data 
        djtext=request.POST.get('text','default')
        
        analyzed = ''
        puntuations = '''.,?!;:'"`-_()[]}<>/{\|@#$%^&*~+=…‽¡¿'''
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
            
        params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed}
        djtext = analyzed
        
    
    if fullCaps =='on':
        analyzed = ''
       
        for char in djtext:
            upChar = char.capitalize()
            analyzed = analyzed + upChar
        params = {'purpose': 'Capitalize text','analyzed_text': analyzed}
        djtext = analyzed
      

    if newLine == 'on':
      
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r': #ye dekho yha \r bhi use karna hoga bcs network me newline ke liye dono use kiye jate hai so if we want to remove newline we have to remove both of them
                analyzed = analyzed+char
        params={'purpose': 'NEW LINE REMOVED','analyzed_text': analyzed}
        djtext = analyzed
       
    if spaceReamove =='on':
        
        analyzed =''
        for char in djtext:
            if char != ' ':
                analyzed = analyzed+char
        params={'purpose': 'Spaces are removed !','analyzed_text': analyzed}
    if removePunc and newLine and fullCaps and spaceReamove =='off':
        return HttpResponse('error no function selected')
        
    return render(request,'analyze.html',params)

def AboutUs(request):
    return HttpResponse("HELLO THERE TECH LOVER , I'm AN INDEPENDENT DEVELOPER LEARNING NEW THIGS HOPE YOU WILL LIKE MY WORK")
def ContactUs(request):
    return HttpResponse('I HOPE YOU LIKED MY WORK HERE IS MY CONTACT INFO \n MAIL - agupta16269@gmail.com \n PHONE NO. - 7307883280')