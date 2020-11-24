from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from recipes import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.user_list),
    url(r'^api/users/$', views.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.getUser),
    path('creators/', views.creator_list),
    url(r'^api/creators/$', views.creator_list),
    url(r'^api/creators/(?P<pk>[0-9]+)$', views.getCreator),
    path('recipes/', views.recipe_list),
    url(r'^api/recipes/$', views.recipe_list), 
    url(r'^api/recipes/(?P<pk>[0-9]+)$', views.getRecipe)

    #path('register/', obtain_jwt_token),

]
