from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home_base.html', {})


def opticTradeLinks(request):
    return render(request, 'home_base.html', {})


def opticalSpares(request):
    return render(request, 'home_base.html', {})


def newTwinkleVision(request):
    return render(request, 'home_base.html', {})


def houseOfBrands(request):
    return render(request, 'home_base.html', {})


def opticalLensLab(request):
    return render(request, 'home_base.html', {})
