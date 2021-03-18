from . import views
from django.urls import include, path

urlpatterns = [

    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('about', views.about, name='about'),
]
