from django.urls import path
from . import views

urlpatterns = [
    path('maqsad/', views.GoalDirectionListAPIView.as_view()),
    path('huquqiy/', views.LegalAPIView.as_view()),
    path('markaz-tarxix/', views.HistoryAPIView.as_view()),
    path('elonlar/', views.AdsListAPIView.as_view()),
    path('yoshlar-siyosati/', views.PoliticsListAPIView.as_view()),
    path('faoliyat-korsatkichlari/', views.ActivityIndicatorAPIView.as_view()),
    path('xalqaro-aloqalar/', views.InternationalContactAPIView.as_view()),
    path('corruption/', views.CorruptionAPIView.as_view()),
]
