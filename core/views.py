from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def index(request):
    return HttpResponse("Welcome to the Core App!")