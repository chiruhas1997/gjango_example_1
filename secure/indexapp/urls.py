from django.urls import path
from . import views

app_name='indexapp'
urlpatterns=[
    path('',views.signin,name='signin'),
    path('login',views.user_login,name="user_login")
]