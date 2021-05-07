
from django.urls import path,include
from . import views
from .views import CreateProduct



urlpatterns = [
    path('creates/',CreateProduct.as_view()),
    path('create/',views.create_form,name="create-form"),
    
]