from django.urls import path
from .views import RecipeListCreateAPIVeiw

app_name = 'api'

urlpatterns = [
    path('recipes/', RecipeListCreateAPIVeiw.as_view(), name='recipe-list-create'),
]
