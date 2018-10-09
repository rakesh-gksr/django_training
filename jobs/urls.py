from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:job_id>', views.detail, name='detail'),
    path('<int:job_id>/update', views.update, name='update'),
]
