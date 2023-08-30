from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import Course, User
from .forms import NewCourseForm, RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    courses = Course.objects.all()
    logged_in = request.COOKIES.get('logged_in')
    user = request.COOKIES.get('name')
    print(user)
    return render(request, "main_app/index.html", {
        "courses": courses,
        "logged_in": logged_in,
        "user": user
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
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            new_object = Course.objects.create(
                name = form.cleaned_data.get("name"),
                description = form.cleaned_data.get("description"),
                image = form.cleaned_data.get("image"),
                slug = slugify(form.cleaned_data.get("name"))
            )
            return redirect('/')
        
    return render(request, "main_app/course_form.html", {
        "course_form": NewCourseForm()
    })

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_object = User.objects.create(
                first_name = form.cleaned_data.get("first_name"),
                last_name = form.cleaned_data.get("last_name"),
                username = form.cleaned_data.get("username"),
                email = form.cleaned_data.get("email"),
                profile_picture = form.cleaned_data.get("profile_picture"),
                password = make_password(form.cleaned_data.get("password"))
            )
            response = redirect('/')
            response.set_cookie('logged_in', True)
            response.set_cookie('name', form.cleaned_data.get("username"))
            return response
        
    return render(request, "main_app/register.html", {
        "register_form": RegisterForm()
    })

def logout(request):
    response = redirect('/')
    response.set_cookie('logged_in', False)
    response.set_cookie('name', '')
    return response

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
          try:
            user = User.objects.get(username=login_form.cleaned_data.get("username"))
          except Exception as exception:
            return HttpResponse("User not found!")
          if check_password(login_form.cleaned_data.get("password"), user.password):
            response = redirect('/')
            response.set_cookie('logged_in', True)
            response.set_cookie('name', user.username)
            return response
          else:
              return HttpResponse("Passwords don't match")
        else:
            return HttpResponse(login_form.errors)
            
    return render(request, "main_app/login.html", {
        "login_form": LoginForm()
    })
