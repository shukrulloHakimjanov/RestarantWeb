from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Q
from django.core.files.storage import default_storage

def home_page(request):
    return render(request, 'home.html')


def about(request):
    about = About.objects.filter().first()
    about2 = About2.objects.all() 
    ser=Service.objects.all()
    context = {
        'about': about,
        'about2': about2,
        'ser':ser,

    }
    return render(request, 'about.html',context)


def service(request):

    client=Clients.objects.all()
    context={
            'client':client
    }
    if request.method=='POST':
        title=request.POST['title']
        stoke=request.POST['stoke']
        description=request.POST['description']
        img=request.FILES['img']
        client=Clients(
            title=title, stoke=stoke, description=description,
            img=img, 
        )
        client.save()
    return render(request, 'service.html',context)

def menu(request):
    q=request.GET.get('q')
    menu=Menu.objects.all()
    if q is not None:
        menu=menu.filter(Q(title__icontains=q))  
    context={
        'menu':menu,
     
    }
    return render(request, 'menu.html' ,context)

def booking(request):
    vidio=Vidio.objects.filter().first()
    context={
        'vidio':vidio
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        data=request.POST.get('data')
        people=request.POST.get('people')
        massange=request.POST.get('text')
        people=Booking(
            name=name,email=email,
            data=data,people=people,
            text=massange,
        )
        people.save()
        msg=f'Dear {name}, Your complaint has been accepted'
        context['message']=msg
    return render(request, 'booking.html' ,context)
def contact(request):
    map=Map.objects.filter().first()
    context={
        'map':map
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        massage=request.POST.get('text')
        contact=ContactUs(
            name=name,email=email,
            subject=subject,text=massage,
        )
        contact.save()
    return render(request, 'contact.html',context)