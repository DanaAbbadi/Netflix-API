from django.urls import path, include
from .views import NetflixList, NetflixDetails

urlpatterns = [
    path('', NetflixList.as_view(), name='netflix'), 
    path('<int:pk>/', NetflixDetails.as_view(), name='netflix_details')  
]