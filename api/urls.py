from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.getRecipes, name="recipes"),
    path('recipes/<str:pk>/', views.getRecipe, name="recipe"),
]
