from django.contrib import admin
from .models import User, Creator, Recipe

class UserList(admin.ModelAdmin):
    list_display = ('user_number', 'name', 'cooking_experience', 'email')
    list_filter = ('user_number', 'name', 'cooking_experience')
    search_fields = ('user_number', 'name')
    ordering = ['user_number']


class CreatorList(admin.ModelAdmin):
    list_display = ('user', 'creator_number', 'creator_title', 'creator_description')
    list_filter = ('user', 'creator_title')
    search_fields = ('user', 'creator_title')
    ordering = ['user']


class RecipeList(admin.ModelAdmin):
    list_display = ('creator', 'recipe_name', 'recipe_description', 'ingredients', 'directions')
    list_filter = ('creator','recipe_name')
    search_fields = ('creator','recipe_name')
    ordering = ['creator']


admin.site.register(User, UserList)
admin.site.register(Creator, CreatorList)
admin.site.register(Recipe, RecipeList)