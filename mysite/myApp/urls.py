from . import views
from django.urls import include, path

urlpatterns = [

    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up')

]
