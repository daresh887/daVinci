from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:page_slug>', views.page)
]