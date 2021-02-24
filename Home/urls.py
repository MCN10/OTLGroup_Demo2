from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.home, name="home"),
	path('OpticTradeLinks', views.opticTradeLinks, name="opticTradeLinks"),
    path('NewTwinkleVision', views.newTwinkleVision, name="newTwinkleVision"),
    path('OpticalSpares', views.opticalSpares, name="opticalSpares"),
	path('HouseOfBrands/', views.houseOfBrands, name="houseOfBrands"),
    path('OpticalLensLab/', views.opticalLensLab, name="opticalLensLab"),
]
