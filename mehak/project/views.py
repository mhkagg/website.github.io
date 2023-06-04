from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .forms import SignupForm,MyForm, SearchForm, LoginForm
from .models import Blogs
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout
import folium
from django.http import HttpResponse
import geocoder
from .models import Search
from django.urls import reverse


@csrf_exempt
def page1(request):
    return render (request, "page1.html", {'navbar': 'page1'})

@csrf_exempt
def page2(request):
    
    return render (request, "page2.html", {'navbar': 'page2'})

@csrf_exempt
def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('page1'))
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'navbar': 'login', 'form': form})


@csrf_exempt
def page3(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page3')
    else:
        form = SearchForm()
    address= Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    m = folium.Map(location=[19, -12], zoom_start=2, max_zoom = 18)
    folium.Marker([lat, lng],tooltip='click for more',icon=folium.Icon(color='red', icon='glyphicon glyphicon-map-marker'), popup=country).add_to(m)
    m = m._repr_html_()
    context={
        'm': m,
        'form': form,
    }
    return render (request, "page3.html", context)

@csrf_exempt
def page4(request):
    return render(request, 'page4.html', {'navbar': 'page4'})


@csrf_exempt
def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(response, "signup.html", context)

@csrf_exempt
def blogs(response):
    mydata = Blogs.objects.all().values()
    if response.method == 'POST':
        form = MyForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = MyForm()
    
    context = {
        'mydata': mydata,
        'form': form
    }
    return render(response, "blogs.html", context)


@csrf_exempt
def signout(request):
    logout(request)
    return redirect("page1")

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = MyForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    return render(request, 'delete_blog.html', {'blog': blog})

def page2(request):
    return render(request, 'page2.html')



def pune(request):
    return render(request, 'pune.html')

def delhi(request):
    return render(request, 'delhi.html')

def manali(request):
    return render(request, 'manali.html')

def assam(request):
    return render(request, 'assam.html')

def mumbai(request):
    return render(request, 'mumbai.html')

def tamil(request):
    return render(request, 'tamil.html')

def kerala(request):
    return render(request, 'kerala.html')

def Sikkim(request):
    return render(request, 'Sikkim.html')

def Andaman(request):
    return render(request, 'Andaman.html')

def AndraPradesh(request):
    return render(request, 'AndraPradesh.html')

def ArunachalPradesh(request):
    return render(request, 'ArunachalPradesh.html')

def Bihar(request):
    return render(request, 'Bihar.html')

def Gujarat(request):
    return render(request, 'Gujrat.html')

def Haryana(request):
    return render(request, 'Haryana.html')



def Jammu(request):
    return render(request, 'Jammu.html')

def karnataka(request):
    return render(request, 'karnataka.html')

def kerala(request):
    return render(request, 'kerala.html')

def Lakhak(request):
    return render(request, 'Lakhak.html')

def Lakshadweep(request):
    return render(request, 'Lakshadweep.html')

def ArunachalPradesh(request):
    return render(request, 'ArunachalPradesh.html')

def MadhayaPradesh(request):
    return render(request, 'MadhayaPradesh.html')

def Meghalaya(request):
    return render(request, 'Maghalaya.html')

def manali(request):
    return render(request, 'manali.html')



def Mizoram(request):
    return render(request, 'Mizoram.html')

def mumbai(request):
    return render(request, 'mumbai.html')

def Nagaland(request):
    return render(request, 'Nagaland.html')

def pune(request):
    return render(request, 'pune.html')

def Odisha(request):
    return render(request, 'Odisha.html')

def Punjab(request):
    return render(request, 'Punjab.html')

def Rajasthan(request):
    return render(request, 'Rajasthan.html')


def UttarPradesh(request):
    return render(request, 'UttarPradesh.html')


def Uttrakhand(request):
    return render(request, 'Uttrakhand.html')

def WestBangal(request):
    return render(request, 'WestBangal.html')
