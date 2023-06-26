from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
    path("", views.Dashboard,name="dashboard"),
    path("additems/", views.InsertPageView,name="insert"),
    path("add/", views.InsertData,name="insert"),
    path("Allitems/", views.ViewItems,name="views"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("update/<int:pk>",views.updateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),  
    
    path("supplier/",views.InsertPageSupp,name="create_supplier"),
    path("adds/", views.create_supplier,name="create_supplier"),
    
    path('purchase/create/', views.create_purchase, name='create_purchase'),
    
    
    
     
   
    
    
    
]