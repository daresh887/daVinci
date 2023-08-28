from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import Course
from .forms import NewCourseForm

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
    
def course_form(request):
    if request.method == "POST":
        print("received")
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")
            new_object = Course.objects.create(
                name = form.cleaned_data.get("name"),
                description = form.cleaned_data.get("description"),
                image = form.cleaned_data.get("image"),
                slug = slugify(form.cleaned_data.get("name"))
            )
            return redirect('/')
        else:
            return HttpResponse(form.errors)
        
    return render(request, "main_app/course_form.html", {
        "course_form": NewCourseForm()
    })
