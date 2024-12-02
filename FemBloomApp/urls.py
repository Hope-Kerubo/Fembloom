
from django.contrib import admin
from django.urls import path
from FemBloomApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('modules', views.modules, name='modules'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('hf', views.hf, name='hf'),
    path('blog', views.blog, name='blog'),
    path('feature', views.feature, name='feature'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('user_dash', views.user_dash, name='user_dash'),
]
