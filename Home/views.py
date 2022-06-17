from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is a Home page")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is a about page")

def services(request):
    return render(request, "services.html")
    #  return HttpResponse("This is services page")

def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("This is contact page")

def pineapple(request):
    return render(request, "pineapple.html")
    
def chocolate(request):
    return render(request, "chocolate.html")    

def strawberry(request):
    return render(request, "strawberry.html")

def vanila(request):
    return render(request, "vanila.html")

def butterscotch(request):
    return render(request, "butterscotch.html")

def blueberry(request):
    return render(request, "blueberry.html")

def cake(request):
    return render(request, "cake.html")

def pastries(request):
    return render(request, "pastries.html")

def doll(request):
    return render(request, "doll.html")

def order(request):
    return render(request, "order.html")