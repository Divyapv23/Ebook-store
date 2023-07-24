from django.shortcuts import render, redirect
from bookapp.models import categorydb, productdb
from frontendapp.models import cartdb, cartaddress, customerdetails
from django.db.models import Sum


# Create your views here.

def homepage(request):
    data = categorydb.objects.all()
    return render(request, "home.html", {'data': data})


def frontcatepage(request, category):
    data = categorydb.objects.all()
    products = productdb.objects.filter(Category=category)
    return render(request, "frontcate.html", {'data': data, 'products': products})


def singleproductpage(request, dataid):
    data = categorydb.objects.all()
    products = productdb.objects.get(id=dataid)
    return render(request, "singleproduct.html", {'data': data, 'products': products})


def cartpage(request):
    data = categorydb.objects.all()
    product = cartdb.objects.all()
    grandtotal = product.aggregate(Sum("Total"))["Total__sum"]
    return render(request, "cart.html", {'data': data, 'product': product, 'grandtotal': grandtotal})


def cartdetails(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        pr = request.POST.get('productprice')
        qt = request.POST.get('qty')
        tl = request.POST.get('totalprice')
        object = cartdb(Name=na, Price=pr, Quantity=qt, Total=tl)
        object.save()
        return redirect(cartpage)


def cartdelete(request, dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)


def cartadddetails(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        ad = request.POST.get('Address')
        st = request.POST.get('State')
        pi = request.POST.get('Pin')
        ml = request.POST.get('Mail')
        nm = request.POST.get('Number')
        object = cartaddress(Name=na, Address=ad, State=st, Zip=pi, Mail=ml, Num=nm)
        object.save()
        return redirect(cartpage)


def userpage(request):
    return render(request, "userlogin.html")


def signuppage(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        ml = request.POST.get('Mail')
        pd = request.POST.get('Password')
        cp = request.POST.get('CPassword')
        object = customerdetails(Name=na, Mail=ml, Password=pd, Confirm=cp)
        object.save()
        return redirect(userpage)


def customerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if customerdetails.objects.filter(Name=username_r, Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            return redirect(homepage)
        else:
            return redirect(userpage)
    return redirect(userpage)


def weblogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)
