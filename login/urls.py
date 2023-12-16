from django.urls import path
from .views import com,ind 
urlpatterns=[
    path('',ind,name= "index"),
    path("praduct/<int:id>/",com, name = "product")

]