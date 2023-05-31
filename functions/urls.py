from django.urls import path
from . import views

urlpatterns = [
    path('funksiya-vazifalari/', views.FunctionAPIView.as_view()),
    path('savol-javob/', views.AnswerAPIView.as_view()),
    path('xizmatlar/', views.XizmatlarAPIView.as_view()),
]
