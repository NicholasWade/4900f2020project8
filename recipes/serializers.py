from rest_framework import serializers
from .models import User, Creator, Recipe


class UserSerializer(serializers.ModelSerializer):

    class Meta:
            model = User
            fields = ('pk', 'user_number', 'user_full_name', 'cooking_experience', 'email')

class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
            model = Creator
            fields = ('pk','user', 'user_number', 'creator_number', 'creator_title', 'creator_description')


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
            model = Recipe
            fields = ('pk','creator', 'creator_number', 'recipe_name', 'recipe_description', 'ingredients', 'directions', 'Category')