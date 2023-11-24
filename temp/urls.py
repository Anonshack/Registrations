from django.urls import path
from .views import HomePage, registration, user_login


urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', user_login, name='login'),
    path('', HomePage.as_view(), name='home'),
]
