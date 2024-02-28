from django.urls import path, include
from .views import GenreList, CrimeList, CrimeCreate, CrimeDetail, SuspectDetail, VictimDetail, TextGenerationView

urlpatterns = [
    path('genres/', GenreList.as_view(), name='genres'),
    path('genres/<int:genre_id>/crimes/', CrimeList.as_view(), name='crimes'),
    path('crimes/<int:pk>/', CrimeDetail.as_view(), name='crime_detail'),
    path('crimes/<int:pk>/generate', TextGenerationView.as_view(), name='generate'),
    path('genres/<int:genre_id>/crimes/create/', CrimeCreate.as_view(), name="crime_create"),
    path('suspect/', SuspectDetail.as_view(), name='suspect'),
    path('victim/', VictimDetail.as_view(), name='victim')
]