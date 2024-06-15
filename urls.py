from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    #path('loader/',views.UserLogin.as_view(), name='loader'),
]