from django.urls import path
from . import views  # Assuming you have views

urlpatterns = [
    # Define your paths here, e.g.,
    # path('', views.home, name='home'),
    # path('job_staff/', views.job_staff, name='job_staff'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    
    
]


