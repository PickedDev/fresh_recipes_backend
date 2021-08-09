from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe
from .serailizers import RecipeSerializer
# Create your views here.


@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serailizer = RecipeSerializer(recipes, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getRecipe(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serailizer = RecipeSerializer(recipe)
        return Response(serailizer.data)
