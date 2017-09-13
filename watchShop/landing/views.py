from django.shortcuts import render

# Create your views here.
def landing(request):
    name = 'Watch Shop'
    return render(request, 'landing/landing.html', locals())
