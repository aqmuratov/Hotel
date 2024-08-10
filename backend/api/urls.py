from django.urls import path
from api.views import HotelView,HotelDetailView,CreateAPIView


urlpatterns = [
    path('',HotelView.as_view(),name='hotels'),
    path('detail/<int:pk>',HotelDetailView.as_view(),name='update'),
    path('create/',CreateAPIView.as_view(),name='create')
]