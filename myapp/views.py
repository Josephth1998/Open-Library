from django.shortcuts import render,redirect
from myapp.models import Genredb,Bookdb
from library.models import Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def addgenre(request):
    return render(request,'addgenre.html')

def savegenre(request):
    if request.method=='POST':
        genre=request.POST.get('genre')
        image=request.FILES['image']
        obj=Genredb(Genre=genre,Image=image)
        obj.save()
    return render(request,'addgenre.html')

def displaygenre(request):
    data=Genredb.objects.all()
    content={
        'data':data
    }
    return render(request,'displaygenre.html',content)

def editgenre(request,dataid):
    data = Genredb.objects.get(id=dataid)
    content = {
        'data': data
    }
    return render(request,'editgenre.html',content)

def updategenre(request,dataid):
    if request.method=="POST":
        genre = request.POST.get('genre')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Genredb.objects.get(id=dataid).Image
        Genredb.objects.filter(id=dataid).update(Genre=genre,Image=file)
        return redirect(displaygenre)

def deletegenre(request,dataid):
    data=Genredb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaygenre)

#Category Books

def addbooks(request):
    data=Genredb.objects.all()
    content={
        'data':data,
    }
    return render(request,'addbooks.html',content)

def savebooks(request):
    if request.method=='POST':
        bname = request.POST.get('bname')
        aname = request.POST.get('aname')
        description = request.POST.get('genre')
        price=request.POST.get('priceperday')
        syno=request.POST.get('synopsis')
        image = request.FILES['image']
        obj=Bookdb(Bookname=bname,Authorname=aname,Description=description,Priceperday=price,Synopsis=syno,Image=image)
        obj.save()
    return render(request,'addbooks.html')

def displaybooks(request):
    data=Bookdb.objects.all()
    content={
        'data':data
    }
    return render(request,'displaybooks.html',content)

def editbooks(request,dataid):
    data = Bookdb.objects.get(id=dataid)
    da=Genredb.objects.all()
    content = {
        'data': data,
        'da':da
    }
    return render(request,'editbooks.html',content)

def updatebooks(request,dataid):
    if request.method=="POST":
        bname = request.POST.get('bname')
        aname = request.POST.get('aname')
        description = request.POST.get('genre')
        price = request.POST.get('priceperday')
        syno = request.POST.get('synopsis')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Bookdb.objects.get(id=dataid).Image
        Bookdb.objects.filter(id=dataid).update(Bookname=bname,Authorname=aname,Description=description,Priceperday=price,Synopsis=syno,Image=file)
        return redirect(displaybooks)

def deletebooks(request,dataid):
    data=Bookdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybooks)

def loginfun(request):
    return render(request,'loginpage.html')

def adminauth(request):
    if request.method=='POST':
        ausername = request.POST.get('username')
        apassword = request.POST.get('password')
        if User.objects.filter(username__contains=ausername).exists():
            user=authenticate(username=ausername,password=apassword)
            if user is not None:
                login(request,user)
                request.session['username']=ausername
                request.session['password']=apassword
                # messages.success(request,"Logged In Successfully !!!")
                return redirect (index)
            else:
                # messages.error(request,"Login credentials dont match. Please Login Again !!!")
                return redirect(loginfun)
        else:
            return redirect(index)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logged Out Successfully !!!")
    return redirect(index)

def displaycontact(request):
    data=Contactdb.objects.all()
    content={
        'data':data
    }
    return render(request,'displaycontact.html',content)

def deletecontact(request,dataid):
    data=Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)



