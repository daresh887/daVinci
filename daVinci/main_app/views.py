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
    try:
        course = Course.objects.get(slug=page_slug)
        return render(request, "main_app/course.html", {
            "course": course
        })
    except Exception as exception:
        return HttpResponse("Aceasta pagina nu exista!")