from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('/home',views.refresh, name='refresh'),
    path('/login',views.login, name='login'),
    path('auth',views.auth,name='auth'),
    path('/main',views.main,name='main'),
    path('/predict',views.predict,name='predict'),
    
    
]
