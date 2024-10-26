from django.urls import path, include
from django.urls import path
from . import views  

urlpatterns = [

    path('register',views.register,name='register'),
    path('',views.login_page,name='login_page'),
    path('logout', views.logout_page, name='logout'),
    path('login_page/', views.login_page, name='login_page'), 
    path('destination/', views.destination, name='destination'),
   

   
    # path('destination/new/', views.destination_create, name='destination_create'),

   
    # path('destination/edit/<int:id>/', views.destination_edit, name='destination_edit'),

   
    # path('destination/<int:id>/', views.destination_detail, name='destination_detail'),

    # path('destination/delete/<int:id>/', views.destination_delete, name='destination_delete'),
]



