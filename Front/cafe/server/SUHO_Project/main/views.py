from django.shortcuts import render

# Create your views here.
def kiosk(request):
    return render(request,'kiosk.html')

def cafemain(request):
    return render(request,'cafemain.html')
