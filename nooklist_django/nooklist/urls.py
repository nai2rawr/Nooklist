from django.urls import path
from . import views
fro, rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

router.register(r'villagers',views.VillagerViewSet, r'recipes', views.RecipesViewSet, r'resources', views.ResourcesViewSet, r'houseware', views.HousewareViewSet, r'clothing', views.ClothingiewSet)
#from django import django_messages

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('houseware-list/', views.houseware_list, name='houseware-list'),
    path('recipes-list/', views.recipes_list, name='recipes-list')
    path('clothing-list/', views.clothing_list, name='clothing-list'),
    path('villager-list/', views.villager_list, name='villager-list'),
    path('resources-list/', views.resources_list, name='resources-list'),
    path('houseware/new', views.houseware_create, name='houseware_create'),
    path('clothing/new', views.clothing_create, name='clothing_create'),
    path('villager/new', views.villager_create, name='villager_create'),
    path('resources/new', views.resources_create, name='resources_create'),
    path('recipes/new', views.recipes_create, name='recipes_create'),
    path('clothing/<int:pk>/edit', views.clothing_edit, name='clothing_edit'),
    path('recipes/<int:pk>/edit', views.recipes_edit, name='recipes_edit'),
    path('resources/<int:pk>/edit', views.resources_edit, name='resources_edit'),
    path('houseware/<int:pk>/edit', views.houseware_edit, name='houseware_edit'),
    path('villager/<int:pk>/edit', views.villager_edit, name='villager_edit'),
    path('houseware/<int:pk>/delete', views.houseware_delete, name='houseware_delete'),
    path('villager/<int:pk>/delete', views.villager_delete, name='villager_delete'),
    path('clothing/<int:pk>/delete', views.clothing_delete, name='clothing_delete'),
    path('resources/<int:pk>/delete',views.resources_delete, name='resources_delete'),
    path('recipes/<int:pk>/delete',views.recipes_delete, name='recipes_delete'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk/>', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message')


]