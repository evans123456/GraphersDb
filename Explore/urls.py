from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'explore'




urlpatterns = [

   
	#explore/
    url(r'^$', views.IndexView.as_view(),name = 'index'),

    #explore/71/
    url(r'^explore/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),


    #explore/add/
    url(r'^image-add/$',views.AddImage.as_view(),name = 'image-add'),

    	

    
]



#after creating a url pattern go create the view.py