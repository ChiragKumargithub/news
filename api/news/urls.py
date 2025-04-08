from django.urls import path
from .views import news_api,home,register_view, login ,logout_view,header_view


urlpatterns = [
    path('',home,name='home'),
    path('news/', news_api, name='news'),
    path('register/',register_view , name='register'),
    path('login/',login , name='login'),
    path('logout/',logout_view , name='logout'),
    path('header/<int:id>/',header_view, name='header')
    
    
]
