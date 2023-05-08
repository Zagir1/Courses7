from django.shortcuts import render, HttpResponse
def home(request):
    return render(request, 'homepage.html')
# Create your views here.
