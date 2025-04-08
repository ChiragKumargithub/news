from django.shortcuts import render ,redirect
from .models import register

import requests

# Create your views here.
def home(request):
             if 'login' in request.session:
                username = request.session['login']
                
                data= {
                     'username': username
                }
                
                return render(request,'home.html',{'loggin':True, 'data':data})
             else:
                return render(request,'home.html') 

def register_view(request):
     if request.method == 'POST':
            obj = register()
            obj.username = request.POST['username']
            obj.email = request.POST['email']
            obj.password = request.POST['password']
            obj.mobile = request.POST['mobile']
            obj.save()
            return render(request, 'register.html')
     else:
           return render(request, 'register.html')
     

def header_view(request,id):
     if 'login' in request.session:
          username = register.objects.get(id = request.POST['username'])
          return redirect('home',{'username': username})
     else:
          return render(request, 'register.html')
               
           

def login(request):
     if request.method == 'POST':
            try:
                registered = register.objects.get(email = request.POST['email'])
                if registered.password == request.POST['password']:
                    request.session['login']= registered.username
                    return redirect('home')
                else:
                    return render(request, 'login.html')
            except:
                    return render(request, 'login.html',{'not_registered':"register phela"}) 
     else:    
           return render(request, 'login.html') 


def logout_view(request):
    del request.session['login']
    return redirect('home')



def news_api(request):
    if 'login' in request.session:
        country = request.GET.get('country')

        API_KEY = 'aa3f833cf3bf4e57af3ad3449f335a20'
    

        url =f"https://newsapi.org/v2/everything?q={country}&apiKey={API_KEY}"
        response= requests.get(url)
        data  = response.json()

        data = data['articles']
        return render(request, 'index.html',{"data":data,'loggin':True})
    else:
        return render(request, 'index.html')  
    