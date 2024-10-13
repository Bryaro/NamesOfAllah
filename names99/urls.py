from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process/', views.process_learning, name='process_learning'),
    path('reset/', views.reset_learning, name='reset_learning'),
    path('learning/', views.learning_page, name='learning_page'),  # Ensure this line is present
    path('mark-as-read/', views.mark_as_read, name='mark_as_read'),  # Ensure this line is present
    path('name/<int:name_id>/', views.name_detail, name='name_detail'),
]

