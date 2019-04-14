from django.urls import path

from .views import ExampleView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('examples/', ExampleView.as_view()),
]