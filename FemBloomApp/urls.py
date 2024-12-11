
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
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz_result', views.user_dash, name='quiz_result'),
    path('donation', views.donation, name='donation'),
    path('donatemoney', views.donatemoney, name='donatemoney'),
    path('donateproducts', views.donateproducts, name='donateproducts'),
    path('sponsorevents', views.sponsorevents, name='sponsorevents'),
]
