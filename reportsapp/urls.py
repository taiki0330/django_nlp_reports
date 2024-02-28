from django.urls import path, include
from .views import GenreList, CrimeList, CrimeCreate, CrimeDetail, SuspectDetail, VictimDetail

urlpatterns = [
    path('genre/', GenreList.as_view(), name='genre'),
    path('crimes/', CrimeList.as_view(), name='crimes'),
    path('crimes/<int:pk>', CrimeDetail.as_view(), name='crime_detail'),
    path('create/', CrimeCreate.as_view(), name="crime_create"),
    path('suspect/', SuspectDetail.as_view(), name='suspect'),
    path('victim/', VictimDetail.as_view(), name='victim')
]