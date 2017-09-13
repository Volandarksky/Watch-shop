from django.shortcuts import render

# Create your views here.
def landing(request):
    name = 'Watch Chop'
    return render(request, 'landing/landing.html', locals())
