from django.urls import path
from .views import UploadCSVAPIView, DatasetHistoryAPIView

urlpatterns = [
    path('upload/', UploadCSVAPIView.as_view(), name='upload-csv'),
    path('history/', DatasetHistoryAPIView.as_view(), name='dataset-history'),
]