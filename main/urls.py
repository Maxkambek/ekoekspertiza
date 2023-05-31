from django.urls import path
from .views import NewsListAPIView, NewsRetrieveAPIView, CalculatorAPIView, SpiritualityListAPIView, \
    BranchSerializerListAPIView, ManagementListAPIView, DirectorListAPIView, DirectorRetrieveAPIView, \
    PartnerListAPIView, DocumentListAPIView, CenterTarkibiListAPIView

urlpatterns = [
    path('list-news/', NewsListAPIView.as_view()),
    path('news-detail/<int:pk>/', NewsRetrieveAPIView.as_view()),
    path('calculator/', CalculatorAPIView.as_view()),
    path('spirituality/', SpiritualityListAPIView.as_view()),
    path('list-branch/', BranchSerializerListAPIView.as_view()),
    path('list-worker/', ManagementListAPIView.as_view()),
    path('list-director/', DirectorListAPIView.as_view()),
    path('detail-director/<int:pk>/', DirectorRetrieveAPIView.as_view()),
    path('partners/', PartnerListAPIView.as_view()),
    path('documents/', DocumentListAPIView.as_view()),
    path('markaz-tarkibi/', CenterTarkibiListAPIView.as_view()),
]
