#THIS FILE IS CREATED BY ME - ARUN
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Hello')


def analyze(request):
    # GET THE TEXT USER ENTERED ON THE WEBSITE
    removePunc = request.GET.get('remove pucuation','off')
    fullCaps = request.GET.get('Capitalizer','off')
    if removePunc =='on':
        djtext=request.GET.get('text', 'default')
        
        analyzed = ''
        puntuations = '''.,?!;:'"`-_()[]}<>/{\|@#$%^&*~+=…‽¡¿'''
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
           
            elif char in puntuations:
                newTxt = djtext.replace(char,'')
                djtext = newTxt
            
        params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
    elif fullCaps =='on':
        analyzed = ''
        djtext = request.GET.get('text','default')
        for char in djtext:
            upChar = char.capitalize()
            analyzed = analyzed + upChar
        params = {'purpose': 'Capitalize text','analyzed_text': analyzed}
        return render(request,'analyze.html',params)



    else:
        return HttpResponse('error')
