from django.shortcuts import render

# Create your views here.
def boot(request):
    return render(request,'boot.html')

def boot2(request):
    return render(request,'boot2.html')
