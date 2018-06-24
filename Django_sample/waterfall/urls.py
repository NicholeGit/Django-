from django.conf.urls import url
from waterfall import views

urlpatterns = [
    url('^img.html$',views.imgs), 
    url('^get_imgs.html$',views.get_imgs), 
   
]