from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    ]
