from django.urls import path
from .views import CreateLoginForm


urlpatterns = [
    path('login/',CreateLoginForm.as_view(),name='login'),
]