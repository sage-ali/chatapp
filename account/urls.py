from django.urls import path
from .views import registerPage, login_view, logout_view

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]