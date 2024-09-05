from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,Payment
from UserApp.models import UserInfo,MyCart,MyWishlist,OrderData,Address
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

# Create your views here.
def home(request):
    cats = Category.objects.all()
    products = Product.objects.all() 
    default_page = 1
    #quant = Product.objects.get()
    page = request.GET.get('page', default_page)
    # Get queryset of items to paginate
    # Paginate items
    paginator = Paginator(products,6)
    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)
    return render(request,"home.html",{"cats":cats,"products":products,"page_obj":items_page,"is_paginated":True,"paginator":paginator})    

def showProducts(request,id):
    cats = Category.objects.all()
    products = Product.objects.filter(category = id) 
    return render(request,"showProducts.html",{"cats":cats,"products":products,"count":request.session})

def viewDetails(request,id):
    cats = Category.objects.all()   
    product = Product.objects.get(id = id)   
    return render(request,"viewDetails.html",{"cats":cats,"product":product}) 

def searchbar(request,):
    if request.method == "GET":
        search = request.GET.get('search')
        products = Product.objects.filter(product_name__icontains = search)
        return render(request,"searchbar.html",{'products':products})

def addToCart(request):
    if "uname" in request.session:
        # to get details of user
        user = UserInfo.objects.get(username=request.session["uname"])
        #to get product details we first fetch id from viewDetails Hidden type  field 
        # and using that id will fetch product details.
        product_id = request.POST["cid"]
        #print(Product.id)
        product = Product.objects.get(id=product_id)
        quantity = request.POST["qntity"]
        size = request.POST['size']
        try:
            item = MyCart.objects.get(user=user,product=product)
        except:
            cart = MyCart()
            cart.user = user
            cart.product = product
            cart.size = size
            cart.quantity = quantity
            cart.save()
            messages.success(request, 'Item added successfully')  
        else:
            messages.error(request,"Item already in cart")     
        return redirect(showAllCartItems)
    else:
        return redirect(login)
    
def addtocart(request):
    if "uname" in request.session:
        user = UserInfo.objects.get(username=request.session["uname"])
        product_id = request.POST["cid"]
        product = Product.objects.get(id=product_id)
        try:
            item = MyCart.objects.get(user=user,product=product)
        except:
            cart = MyCart()
            cart.user = user
            cart.product = product
            cart.quantity = 1
            cart.size = "M"
            cart.save()
            messages.success(request, 'Item added successfully')       
        else:
            messages.error(request,"Item already in cart")
        return redirect(showAllCartItems)
    else:
        return redirect(login)
    
def showAllCartItems(request):
    if request.method == "GET":
        items = MyCart.objects.filter(user=request.session["uname"])
        global count 
        count = 0
        total = 0
        for item in items:
            count += 1
            total += item.quantity * item.product.price
        request.session["total"]=total
        request.session["count"]=count
        return render(request,"showAllCartItems.html",{"items":items,"total":total,"count":count})
    else:
        product_id = request.POST['product_id']
        item = MyCart.objects.get(id=product_id)
        action = request.POST.get("action")
        if action == "update":
            qntity = request.POST["qntity"]
            size = request.POST['size']
            item.quantity = qntity
            item.size = size
            item.save()
            return redirect(showAllCartItems)
        elif action == "remove":
            item.delete()
            return redirect(showAllCartItems)
        else:
            return redirect(makePayment)
        
def makePayment(request):
    if request.method == "GET":
        if "uname" in request.session:
            try:
               details = Address.objects.get(name_id=request.session["uname"])
            except:
               return redirect(address)
            else:
                count = request.session.get("count")
                details = Address.objects.filter(name_id=request.session["uname"])
                return render(request,"makePayment.html",{"details":details,"count":count})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        
        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry) 
        except:
            messages.error(request,"Invalid card details")
            return render(request,"makePayment.html",{})
        else:
            owner = Payment.objects.get(card_no="222",cvv="202",expiry="12/2025")
            buyer.balance -= float(request.session["total"]) 
            owner.balance += float(request.session["total"])
            buyer.save()
            owner.save()
            
            myOrder = OrderData()
            user = UserInfo.objects.get(username=request.session["uname"])
            myOrder.user = user
            #myOrder.date = OrderData.date
            
            items = MyCart.objects.filter(user=user)
            details = ""
            for item in items:
                details += item.product.product_name+", " 
                item.delete()
            myOrder.amount = request.session["total"]
            myOrder.details = details
            myOrder.save()
            count = request.session.get("count")
            details = Address.objects.filter(name_id=request.session["uname"])
            return render(request,"thankYou.html",{"count":request.session})
    
def showProfile(request):
    if "uname" in request.session:
        return render(request,"showProfile.html",{})

def addToWishlist(request):
    if "uname" in request.session:
        user = UserInfo.objects.get(username=request.session["uname"])
        product_id = request.POST["cid"]
        product = Product.objects.get(id=product_id)
        try:
            item = MyWishlist.objects.get(user_id=user,product_id=product)
        except:
            cart = MyWishlist()
            cart.user = user
            cart.product = product
            cart.save()
            messages.info(request, 'Item wishlisted')                   
        else:
            messages.error(request,"Item already in wishlist")
        return redirect(home)
    else:
        return redirect(login)    

def showAllWishlist(request):
    if request.method == "GET":
        items = MyWishlist.objects.filter(user=request.session["uname"])
        return render(request,"showAllWishlist.html",{"items":items})
    else:
        product_id = request.POST['product_id']
        item = MyWishlist.objects.get(id=product_id)
        action = request.POST.get("action")
        if action == "remove":
            item.delete()
            return redirect(showAllWishlist)

def logout(request):
    request.session.clear()
    return redirect(home)

def login(request):
    if request.method == "GET":
        return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            UserInfo.objects.get(username=uname,password=pwd)
        except:
            message = "Invalid Credentials, Please Login Again!"
            return render(request,"login.html",{"message":message})
        else:
            request.session["uname"] = uname
            return redirect(home)

def signUp(request):
    if request.method == "GET":
        return render(request,"signUp.html",{})
    else:
        uname = request.POST["uname"]
        uname = uname.split(" ")
        pwd = request.POST["pwd"]
        try:
            UserInfo.objects.get(username = uname[0])
        except:               
            user = UserInfo(uname[0],pwd)
            user.save()
            request.session["uname"] = uname[0]
            return redirect(home)
        else:
            message = "This user already exists"
            return render(request,"signUp.html",{"message":message})

def address(request):
    if request.method == "GET": 
        details = Address.objects.filter(name=request.session["uname"])
        return render(request,"address.html",{"details":details})
    else:
        fname = request.POST["fname"]
        email = request.POST["email"]
        addr = request.POST["addr"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        mobile = request.POST["mobile"]
        name_id = request.session["uname"]
        try:
            user = Address.objects.get(name=request.session["uname"])
        except:
            user = Address()
            user.fname = fname
            user.email = email
            user.addr = addr
            user.city = city
            user.state = state
            user.zip = zip
            user.mobile = mobile
            user.name_id = name_id
            user.save()
            messages.success(request, 'Address Saved')       
            return redirect(home)
        else:
            user.fname = fname
            user.email = email
            user.addr = addr
            user.city = city
            user.state = state
            user.zip = zip
            user.mobile = mobile
            user.save()
            messages.success(request, 'Address Updated')       
            return redirect(home)

def yourOrders(request):
    cats = Category.objects.all()   
    orders = OrderData.objects.filter(user = request.session["uname"])
    return render(request,"summary.html",{"cats":cats,"orders":orders})     

