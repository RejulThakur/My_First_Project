from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout 
from django.shortcuts import render,redirect
from .models import sign,products,category,slider,glass,shape,banner,cart,wishlist
from django.contrib.auth.models import User
from django.contrib.auth import hashers
import os



def lo(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password=hashers.make_password(password)
        User.objects.create(username=name,email=email,password=password)
        g=glass.objects.all()
    return render(request,'s.html',{'data':g})



def log(request): 
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        # user=sign.objects.filter(email=email,password=password)
        Users=authenticate(username=email,password=password)
        print(email,password,Users)
        if Users is not None:
            login(request, Users)
        d=category.objects.all()
        sl=slider.objects.all()
        g=glass.objects.all()
        for sd in sl:
            sd.image=os.path.basename(sd.image.url)
            for j in d:
                j.image1=os.path.basename(j.image1.url)
                return render(request,'index.html',{'data1':d,'slider':sl,'data2':g})
            return render(request,'index.html')
        else:
            return render(request,'s.html')
        # if users:
        #     return render(request,'index.html',{"name":users[0].name})
    return render(request,'s.html')

def logoutUser(request):

    logout(request)

    d=category.objects.all()
    sl=slider.objects.all()
    g=glass.objects.all()
    for sd in sl:
        sd.image=os.path.basename(sd.image.url)
    for j in d:
        j.image1=os.path.basename(j.image1.url)
    return render(request,'index.html',{'data1':d,'slider':sl,'data2':g})

def si(request):
    return render(request,'s.html')

def track(request):
    g=glass.objects.all()
    return render(request,'track.html',{'data2':g[:5]})

def home(request):
    d=category.objects.all()
    sl=slider.objects.all()
    g=glass.objects.all()
    s=shape.objects.all()
    b=banner.objects.exclude(banner_name='default')
    print(b)
    for shpe in s:
        shpe.image=os.path.basename(shpe.image.name)
    for sd in sl:
        sd.image=os.path.basename(sd.image.url)
    for j in d:
        j.image1=os.path.basename(j.image1.url)
    for i in b:
        i.banner_image=os.path.basename(i.banner_image.url)
    return render(request,'index.html',{'data1':d[:5],'slider':sl,'data2':g[:5],'data3':s[:4],'data4':b})


def pwr(request):
    a=products.objects.all()
    for b in a:
        b.image2=os.path.basename(b.image2.url)
    return render(request,'pw.html',{'data3':a})

def sun(request):
    return render(request,'sungl.html')

def po(request):
    return render(request,'pw.html')


def eyeglass(request):
    if request.method=="POST":
        category1=request.POST.get("category")
        print(category1.title())
        g=glass.objects.all()
        cat=category.objects.get(category_name=category1.title())
        if cat:
            data=products.objects.filter(category_name=cat)
            print(data)
            for i in data:  
                i.image=os.path.basename(i.image.name)
                print(i.category_name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,'pw.html')


def sun(request):
    sung=products.objects.all()
    for s in sung:
        s.image=os.path.basename(s.image.name)
    return render(request,'sungl.html',{'data':sung})
        
def detail(request):
    if request.method=="POST":
        print("hello")
        g=glass.objects.all()
        title1=request.POST.get('title')
        p=products.objects.filter(title=title1)
        print(title1,p)
        for i in p:
            i.image2=os.path.basename(i.image2.name)
            i.image3=os.path.basename(i.image3.name)
            i.image4=os.path.basename(i.image4.name)
            i.image5=os.path.basename(i.image5.name)
            i.image6=os.path.basename(i.image6.name)
            i.image7=os.path.basename(i.image7.name)
            i.image8=os.path.basename(i.image8.name)
            i.image9=os.path.basename(i.image9.name)
            i.image10=os.path.basename(i.image10.name)
            i.image11=os.path.basename(i.image11.name)
            i.airess1=os.path.basename(i.airess1.name)
            i.airess2=os.path.basename(i.airess2.name)
            i.airess3=os.path.basename(i.airess3.name)
            i.airess4=os.path.basename(i.airess4.name)
            i.airess5=os.path.basename(i.airess5.name)
            i.airess6=os.path.basename(i.airess6.name)
            i.airess7=os.path.basename(i.airess7.name)
            i.airess8=os.path.basename(i.airess8.name)
            i.airess9=os.path.basename(i.airess9.name)
        return render(request,'product detail.html',{'data':p,'data2':g[:5]})
    

def profile(request):
    return render(request,'profile.html')



def round(request):
    if request.method=="POST":
        category1=request.POST.get("shape")
        print(category1)
        s=shape.objects.all()
        g=glass.objects.all()
        cat=shape.objects.get(shape_name=category1)
        if cat:
            data=products.objects.filter(shape_name=cat)
            print(data)
            for i in data:  
                i.image=os.path.basename(i.image.name)
                print(i.shape_name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,'pw.html')

def john(request):
    if request.method=="POST":
        category3=request.POST.get("banner")
        print(category3)
        g=glass.objects.all()
        cat1=banner.objects.get(banner_name=category3)
        print(cat1)
        if cat1: 
            data=products.objects.filter(banner_name=cat1)
            print(data,"hello")
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,('index.html'))
        

def trending(request):
    if request.method=="POST":
        category2=request.POST.get("banner")
        print(category2)
        g=glass.objects.all()
        cat2=banner.objects.get(banner_name=category2)
        print(cat2)
        if cat2: 
            data=products.objects.filter(banner_name=cat2)
            print(data)
            for i in data:
                i.image=os.path.basename(i.image.name)
                print(i.banner_name)
        return render(request,'eyeglasses.html',{'data':data,'data2':g[:5]})
    return render(request,('index.html'))

def ct(request):
    print("hey")
    g=glass.objects.all()
    if request.method=="POST":
       qty=request.POST.get('qyt')
       name=request.POST.get('proname')
       print(name)
       tpro=products.objects.get(pro_d=name)
       print(tpro)
       price=request.POST.get('price')
       print(price)
       tp=int(price) * int(qty)
       cart.objects.create(pro_d=tpro,quantity=qty,user=request.user,price=tp)
    data=cart.objects.filter(user=request.user)
    for i in data:
          i.pro_d.image=os.path.basename(i.pro_d.image.name)
    return render(request,'cart.html',{'data':data,'data2':g[:5]})

def wish(request):
    print("wishh")
    g=glass.objects.all()
    if request.method=="POST":
        wname=request.POST.get('proname')
        print(wname)
        wpro=products.objects.get(pro_d=wname)
        print(wpro)
        price=request.POST.get('price')
        print(price)
        g=glass.objects.all()
        wishlist.objects.create(pro_d=wpro,price=price,user_id=request.user)
    data3=wishlist.objects.filter(user_id=request.user)
    for i in data3:
        i.pro_d.image=os.path.basename(i.pro_d.image.name)
    return render(request,'wishlist.html',{'data':data3,'data2':g[:5]})  


def contaact(request):
    g=glass.objects.all()
    return render(request,'contact.html',{'data2':g[:5]})