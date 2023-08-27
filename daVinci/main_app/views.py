from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, "main_app/index.html", {
        "courses": courses
    })

def page(request, page_slug):
    return HttpResponse(page_slug)