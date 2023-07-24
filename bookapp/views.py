from django.shortcuts import render, redirect
from bookapp.models import categorydb, productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from frontendapp.models import cartdb, cartaddress


# Create your views here.

def indexpage(request):
    return render(request, "index.html")


def categorypage(request):
    return render(request, "category.html")


def categorydetails(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        img = request.FILES['Image']
        des = request.POST.get('description')
        obj = categorydb(Name=na, Image=img, Descript=des)
        obj.save()
        return redirect(indexpage)


def catedisplaypage(request):
    data = categorydb.objects.all()
    return render(request, "displaycategory.html", {'data': data})


def editcatepage(request, dataid):
    data = categorydb.objects.get(id=dataid)
    return render(request, "editcategory.html", {'data': data})


def updatecatepage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('Name')
        ds = request.POST.get('Descript')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=na, Image=file, Descript=ds)
        return redirect(catedisplaypage)


def delcatepage(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(catedisplaypage)


def productpage(request):
    data = categorydb.objects.all
    return render(request, "product.html", {'data': data})


def productdetails(request):
    if request.method == "POST":
        bna = request.POST.get('Name')
        ana = request.POST.get('Authname')
        cat = request.POST.get('Category')
        img = request.FILES['Image']
        lag = request.POST.get('Language')
        des = request.POST.get('Descript')
        pr = request.POST.get('Price')
        obj = productdb(Bname=bna, Aname=ana, Category=cat, Image=img, Lang=lag, Descript=des, Price=pr)
        obj.save()
        return redirect(productpage)


def pdtdispage(request):
    data = productdb.objects.all()
    return render(request, "displayproduct.html", {'data': data})


def editpdtpage(request, dataid):
    data = categorydb.objects.all()
    products = productdb.objects.get(id=dataid)
    return render(request, "editproduct.html", {'data': data, 'products': products})


def updatepdtpage(request, dataid):
    if request.method == "POST":
        bna = request.POST.get('Name')
        ana = request.POST.get('Authname')
        cat = request.POST.get('Category')
        lag = request.POST.get('Language')
        des = request.POST.get('Descript')
        pr = request.POST.get('Price')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Bname=bna, Aname=ana, Category=cat, Image=file, Lang=lag,
                                                   Descript=des, Price=pr)
        return redirect(pdtdispage)


def delpdt(request, dataid):
    data = productdb.objects.get(id=dataid)
    data.delete()
    return redirect(pdtdispage)


def displaycart(request):
    data = cartdb.objects.all()
    product = cartaddress.objects.all()
    return render(request, "cartdisplay.html", {'data': data, 'product': product})
