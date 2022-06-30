from xml.etree.ElementInclude import include
from django.urls import path

from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('showdiary/',views.showdiary, name='showdiary'),
    path('singlediary/<str:id>/',views.singlediary, name='singlediary'),
    path('updatediary/<str:id>/',views.updatediary, name='updatediary'),
    path('deletediary/<str:id>/',views.deletediary, name='deletediary'),
]

   