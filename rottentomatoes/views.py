from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def movie_details(request, id):
    return render(request, 'movie_details.html', {"id": id})
