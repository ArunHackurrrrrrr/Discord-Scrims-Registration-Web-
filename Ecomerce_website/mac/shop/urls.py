from django.urls import path
from .import views
urlpatterns = [
    path("",views.index, name='ShopHome'),
    path("aboutus/",views.aboutUs, name='AboutUs'),
    path("contactus/",views.contactUs, name='ContactUs'),
    path("tracker/",views.trackOrder, name='TrackingStatus'),
    path("search/",views.search, name='Search'),
    path("prodview/",views.prodView, name='ProductView'),
    path("checkout/",views.checkOut, name='CheckOut'),
]
