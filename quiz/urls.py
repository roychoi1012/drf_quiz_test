from django.urls import path
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("random/<int:id>/", randomQuiz),
]