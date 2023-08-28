from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('<slug:page_slug>', views.page),
    path('create_course/', views.course_form)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)