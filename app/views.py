from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
#Import Pagination Stuff
from django.core.paginator import Paginator
import requests, json
# Datetime
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
            
    else:
        my_orders = 0
    # Rated Elements
    rated_dict = {}
    numbers = []
    rateds = {}
    
    for p in Product.objects.all():
        prodView = len(Views.objects.filter(prod=p))
        rated_dict[p]=prodView
        numbers.append(prodView)
    if len(numbers)>12:
        while len(rateds) <= 12:
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                   
                    rateds[key]=value
            numbers.remove(maximum)
    else:
        while len(rateds) <= len(numbers):
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                    
                    rateds[key]=value
            numbers.remove(maximum)
    # Nav elements
    cat = Category.objects.all()
    prods = Product.objects.filter(fire_index=True)
    products = []
    product = Product.objects.all().order_by("id")
    for p in product:
        if len(products)<=3:
            products.append(p)
    # Paginator elements
    
    # Sale
    bests = []
    best = Product.objects.filter(best=True)
    for b in best:
        if len(bests)<=3:
            bests.append(b)
    news = []
    for p in  Product.objects.all():
        if p.Days_till < 30:
            if len(news)<=3:
                news.append(p) 
    
    return render(request,'home.html',{
        "cat":cat,
        "prods":prods,
        "news":news,
        "bests":bests,
        "rateds":rateds,
        "products":products,
        "my_orders":my_orders
    })

def categoryHome(request,id):
   # My order count
    if request.user.is_authenticated:
        my_order = []
  
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    if int(id)==2:
        best = Product.objects.filter(best=True)
        category = Category.objects.get(pk=int(id))
        products = []
        product = Product.objects.all().order_by("id")
        for p in product:
            if len(products)<=3:
                products.append(p)
        # Rated Elements
        rated_dict = {}
        numbers = []
        rateds = {}
        
        for p in Product.objects.all():
            prodView = len(Views.objects.filter(prod=p))
            rated_dict[p]=prodView
            numbers.append(prodView)
            if len(numbers)>12:
                while len(rateds) <= 12:
                    maximum = max(numbers)
                    for key,value in rated_dict.items():
                        if value==maximum:
                        
                            rateds[key]=value
                    numbers.remove(maximum)
            else:
                while len(rateds) <= len(numbers):
                    maximum = max(numbers)
                    for key,value in rated_dict.items():
                        if value==maximum:
                            
                            rateds[key]=value
                    numbers.remove(maximum)
        return render(request,"printed_in.html",{
            "category":category,
            "best":best,
            "products":products,
            "rateds":rateds,
            "my_orders":my_orders
        })
    else:
        category = Category.objects.get(pk=int(id))
        quality = Quality.objects.filter(cat=category)
        palets = []
        for p in Product.objects.all():
            if p.quality in quality and p.design.palet not in palets:
                palets.append(p.design.palet)
        return render(request,"cat_home.html",{
            "category":category,
            "products":palets,
            "my_orders":my_orders
        })

def designs(request,id):
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0

    palet = Palet.objects.get(pk=id)
    design = Design.objects.filter(palet=palet)
    products = []
    for d in design:
        for p in (Product.objects.filter(design=d)):
            products.append(p)
    design =Paginator(products,12)
    design_page = request.GET.get("page")
    designs = design.get_page(design_page)
    design_nums = "a"*designs.paginator.num_pages
    return render(request,"designs.html",{
        "palet":palet,
        "my_orders":my_orders,
        "designs":designs,
        "design_nums":design_nums
    })


def homHotel(request,id):
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    
    if int(id) == 1:
        name = "Hotel"
        palets = []
        for p in Product.objects.filter(type="HOTEL"):
            if p.design.palet not in palets:
                palets.append(p.design.palet)
    else:
        name = "Home"
        palets = []
        for p in Product.objects.filter(type="HOME"):
            if p.design.palet not in palets:
                palets.append(p.design.palet)
    
    return render(request,'home_hotel.html',{
        "name":name,
        "products":palets,
        "my_orders":my_orders  
    })

def Best(request):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    best = Paginator(Product.objects.filter(best=True),12)
    best_page = request.GET.get('page')
    products = best.get_page(best_page)
    prod_nums = "a" * products.paginator.num_pages
    return render(request,'best.html',{
        "products":products,
        "prod_nums":prod_nums,
        "my_orders":my_orders
    })

def Categorys(request):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0

    prod = Paginator(Product.objects.all(),12)
    product_page = request.GET.get('page')
    products = prod.get_page(product_page)
    prod_nums = "a"*products.paginator.num_pages
    
    return render(request,'categorys.html',{
        "products":products,
        "prod_nums":prod_nums,
        "my_orders":my_orders
    })



def Saling(request):
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    
    news = []
    for p in  Product.objects.all():
        if p.Days_till < 30:
            news.append(p) 
    best = Paginator(news,12)
   
    best_page = request.GET.get('page')
    products = best.get_page(best_page)
    prod_nums = "a" * products.paginator.num_pages
    return render(request,'news.html',{
        "products":products,
        "prod_nums":prod_nums,
        "my_orders":my_orders
    })
    

def Printed_Carpets(request,type):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    # Pprinted Categorys
    if type=="HOME":
        products = Product.objects.filter(type="HOME")
    else:
        products = Product.objects.filter(type="HOTEL")
    # Nav elements
    cat = Category.objects.all()
    prods = Product.objects.filter(fire_index=True)
    return render(request,"categorys.html",{
        "prods":prods,
        "cat":cat,
        "category":type,
        "carpets":products,
        "my_orders":my_orders
    })



def More(request,carpet_id): 
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    
    best = Product.objects.filter(best=True)
    # Rated Elements
    rated_dict = {}
    numbers = []
    rateds = {}
    
    for p in Product.objects.all():
        prodView = len(Views.objects.filter(prod=p))
        rated_dict[p]=prodView
        numbers.append(prodView)
    if len(numbers)>12:
        while len(rateds) <= 12:
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                   
                    rateds[key]=value
            numbers.remove(maximum)
    else:
        while len(rateds) <= len(numbers):
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                    
                    rateds[key]=value
            numbers.remove(maximum)
    products = []
    product = Product.objects.all().order_by("id")
    for p in product:
        if len(products)<=3:
            products.append(p)
    product = Product.objects.get(pk=carpet_id)
    # Views parameter
    views =Views.objects.filter(prod=product).count()
    # More Elements 
    
    # Nav elements
    photos = Product.objects.filter(design=product.design)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))*100
        order = ClientOrder(
            user = request.user,
            product=product,
            quantity = quantity
        )
        order.save()
        return redirect('cart')
    return render(request,'more.html',{
       "photos":photos,
       "product":product,
       "views":views,
       "rateds":rateds,
       "products":products,
       "best":best,
       "my_orders":my_orders
    })


def Search(request):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
    else:
        my_orders = 0
    products = Product.objects.all()
    return render(request,'searched.html',{
        "products":products,
         "my_orders":my_orders
            
    })
    
def Buy(request,id):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        my_orders = 0
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
                my_orders = len(my_order)
    else:
        my_orders = 0
    
    best = Product.objects.filter(best=True)
    # Rated Elements
    rated_dict = {}
    numbers = []
    rateds = {}
    
    for p in Product.objects.all():
        prodView = len(Views.objects.filter(prod=p))
        rated_dict[p]=prodView
        numbers.append(prodView)
    if len(numbers)>12:
        while len(rateds) <= 12:
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                   
                    rateds[key]=value
            numbers.remove(maximum)
    else:
        while len(rateds) <= len(numbers):
            maximum = max(numbers)
            for key,value in rated_dict.items():
                if value==maximum:
                    
                    rateds[key]=value
            numbers.remove(maximum)
    products = []
    product = Product.objects.all().order_by("id")
    for p in product:
        if len(products)<=3:
            products.append(p)
    product = Product.objects.get(pk=id)
    # Views parameter 

    # GEO ip
    ip = requests.get("https://api.ipify.org?format=json")
    loc = ip.text
    location_data = json.loads(loc)
    for k, v in location_data.items():
        t=v
    if Views.objects.filter(prod=product):
        ips = []
        for i in Views.objects.filter(prod=product):
            ips.append(i.client.ip)
        if t not in ips:
            view = Views(
                prod = product,
                client = OurCustomers.objects.get(ip=t)        
            )
            view.save()
    else:
        view = Views(
            prod = product,
            client = OurCustomers.objects.get(ip=t)               
        )
        view.save()
    views =Views.objects.filter(prod=product).count()
    # Nav elements
    photos = Product.objects.filter(design=product.design)
    # Add Card Product form 
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))*100
        order = ClientOrder(
            user = request.user,
            product=product,
            quantity = quantity
        )
        order.save()
        return redirect('cart')

    return render(request,'buying_prod.html',{
       "photos":photos,
       "product":product,
       "views":views,
       "rateds":rateds,
       "products":products,
       "best":best,
       "my_orders":my_orders
    })


def Purchase(request):
    user = request.user
    if request.method == "POST":
        num = request.POST.get("phone")
        carts = ClientOrder.objects.filter(user=user)
        for cart in carts:
            if cart.phone == None:
                cart.phone = num
                cart.save()
        return redirect("cart")
    
def Cart(request):
    # My order count
    if request.user.is_authenticated:
        my_order = []
        cart = []
        orders = ClientOrder.objects.filter(user=request.user)
        for order in orders:
            if order.phone == None:
                my_order.append(order)
        my_orders = len(my_order)
        for c in orders:
            if c.user == request.user and c.phone==None:
                cart.append(c)
    else:
        my_orders = 0
        cart = None
    
    return render(request,'cart.html',{
        "cart":cart,
        "my_orders":my_orders
    })


def Remove(request,id):
    buying = ClientOrder.objects.get(pk=id)
    buying.delete()
    return redirect("cart")


def Clear_Order(request):
    buying = ClientOrder.objects.filter(user=request.user)
    for buy in buying:
        buy.delete()
    return redirect("home")


def userLogin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,("There Was an Error Logging In , Try Again..."))
            return redirect('login')
    else:
        return render(request,'users/login.html',{})

def userSignup(request):
    return render(request,'users/signup.html',{})

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser(
            first_name = name,
            last_name = name,
            username=name,
            email=email,
            password = password
        )
        user.save()
        login(request,user)
        return redirect("home") 

def logout_user(request):
    logout(request)
    messages.success(request, ("You were Logged Out!"))
    return redirect('home')
