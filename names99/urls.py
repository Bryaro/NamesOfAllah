from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
    path('process/', views.process_learning, name='process_learning'),  # URL for processing form
]
