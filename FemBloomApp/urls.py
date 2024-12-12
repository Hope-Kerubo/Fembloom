
from django.contrib import admin
from django.urls import path
from FemBloomApp import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('selection', views.selection, name='selection'),
    path('get_institutions/', views.get_institutions, name='get_institutions'),
    path('m1/', views.m1, name='m1'),
    path('m2/', views.m2, name='m2'),
    path('m3/', views.m3, name='m3'),
    path('m4/', views.m4, name='m4'),
    path('donationsapplication/', views.apply_donation, name='donationsapplication'),
    path('sponsor_event/<int:event_id>/', views.sponsor_event, name='sponsor_event'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('events/', views.upcoming_events, name='events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
