from django.shortcuts import render,redirect
from myapp.models import Genredb, Bookdb
from library.models import Userdbook, Contactdb

# Create your views here.
def libindex(request):
    data=Genredb.objects.all()
    return render(request,'libindex.html',{'data':data})
def displaycategoryfun(request,itemcat):
    print("===itemcat===", itemcat)
    cat = itemcat.upper()
    data = Genredb.objects.all()
    book = Bookdb.objects.filter(Description=itemcat)

    context = {
        'data':data,
        'cat':cat,
        'book':book,
    }
    return render(request, "displaycategory.html",context)
def booksinglefun(request,dataid):
    data1=Bookdb.objects.get(id=dataid)
    da= Genredb.objects.all()
    return render(request,"booksingle.html",{'data1':data1,'da':da})

def userreg(request):
    return render(request,'userregister.html')


def registersave(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        ema=request.POST.get('email')
        psd=request.POST.get('pwd')
        cpsd=request.POST.get('cpwd')
        if psd==cpsd:
            obj=Userdbook(Uname=name,Email=ema,Password=psd,Cpassword=cpsd)
            obj.save()
            return redirect(libindex)
        else:
            return render(request,'userregister.html',{'msg':" Sorry , Password Does Not Match . Please Sign In Again !" })

#login fns

def userlogin(request):
    return render(request,'userlogin.html')

def userloginsave(request):
    if request.method=='POST':
        username=request.POST.get("uname")
        password=request.POST.get("pwd")

        if Userdbook.objects.filter(Uname=username,Password=password).exists():
            request.session['uname']=username
            request.session['pwd']=password
            return redirect(libindex)
        else:
            return render(request,'userlogin.html',{'msg':" Sorry , Password Does Not Match . Please Login Again !" })
    else:
        return redirect(libindex)

def userlogout(request):
    del request.session['uname']
    del request.session['pwd']
    # messages.success(request,"Logged Out Successfully !!!")
    return redirect(libindex)

def contact(request):
    da = Genredb.objects.all()
    return render(request,"contact.html", {'da':da})

def contactsave(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        ema = request.POST.get('emailid')
        msg = request.POST.get('message')
        obj = Contactdb(Username=nam, Emailid=ema, Message=msg)
        obj.save()
    return redirect(libindex)

