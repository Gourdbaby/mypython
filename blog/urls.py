from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='blog'
urlpatterns = [
    path('insertcontent/',views.insertcontent),
    path('getcontent/',views.getcontent),
    path('delcontent/',views.delcontent),
    path('updatecontent/',views.updatecontent)
]
 