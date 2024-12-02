from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def modules(request):
    return render(request, 'modules.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def blog(request):
    return render(request, 'blog.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def hf(request):
    return render(request, 'hf.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def user_dash(request):
    return render(request, 'user_dash.html')
