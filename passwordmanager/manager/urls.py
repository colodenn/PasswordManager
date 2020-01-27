from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/passwordform', views.changepassword, name="changepassword"),
    path('dashboard/deletepassword', views.deletepassword, name="deletepassword"),
    path('dashboard/addpassword', views.addpassword, name="addpassword")



    
]