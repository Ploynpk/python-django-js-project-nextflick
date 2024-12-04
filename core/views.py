from django.shortcuts import render

# Create your views here.
def index(request):
    #rendering html file
    return render(request, 'index.html')


    