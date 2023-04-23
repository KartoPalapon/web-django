from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('home', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('feature/', views.feature, name='feature'),
    path('subscription', views.subscription, name='subscription'),
    path('subscription/thankyou', views.subscription_thankyou, name='subscription_thankyou'),
]