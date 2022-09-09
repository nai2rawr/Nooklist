from django.shortcuts import render, redirect
from .forms import HousewareForm, VillagerForm, RecipesForm, ResourcesForm, ClothingForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer
User = get_user_model()

def resources_create(request):
    if request.method == 'POST':
        form = ResourcesForm(Request.POST)
        if form.is_valid():
            resources = form.save()
            return redirect('resources_detail',pk=resources.pk)
        else:
            form = ResourcesForm()
        return render(request, 'nooklist/resources_form.html', {'form': form})


def recipes_create(request):
    if request.method == 'POST':
        form = RecipesForm(Request.POST)
        if form.is_valid():
            recipes = form.save()
            return redirect('recipes_detail', pk=recipes.pk)
        else:
            form = RecipesForm()
        return render(request, 'nooklist/recipes_form.html', {'form': form})


def villager_create(request):
    if request.method == 'POST':
        form = VillagerForm(Request.POST)
        if form.is_valid():
            villager = form.save()
            return redirect('villager_detail', pk=villager.pk)
        else:
            form = VillagerForm()
        return render(request, 'nooklist/villager_form.html', {'form': form})


def clothing_create(request):
    if request.method == 'POST':
        form = ClothingForm(Request.POST)
        if form.is_valid():
            clothing = form.save()
            return redirect('clothing_detail', pk=clothing.pk)
        else:
            form = ClothingForm()
        return render(request, 'nooklist/clothing_form.html', {'form': form})


def houseware_create(request):
    if request.method == 'POST':
        form = HousewareForm(Request.POST)
        if form.is_valid():
            houseware = form.save()
            return redirect('houseware_detail', pk=houseware.pk)
        else:
            form = HousewareForm()
        return render(request, 'nooklist/houseware_form.html', {'form': form})

def houseware_edit(request, pk):
    houseware = Houseware.objects.get(pk = pk)
    if request.method == 'POST':
        form = HousewareForm(request.POST, instance=houseware)
        if form.is_valid():
            houseware = form.save()
            return redirect('houseware_detail', pk = houseware.pk)
        else:
            form = HousewareForm(instance=houseware)
        return render(request, 'nooklist/houseware_form.html'{'form':form})


def clothing_edit(request, pk):
    clothing = Clothing.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClothingForm(request.POST, instance=clothing)
        if form.is_valid():
            clothing = form.save()
            return redirect('clothing_detail', pk=clothing.pk)
        else:
            form = ClothingForm(instance=clothing)
        return render(request, 'nooklist/clothing_form.html'{'form': form})


def villager_edit(request, pk):
    villager = Villager.objects.get(pk=pk)
    if request.method == 'POST':
        form = VillagerForm(request.POST, instance=villager)
        if form.is_valid():
            villager = form.save()
            return redirect('villager_detail', pk=villager.pk)
        else:
            form = VillagerForm(instance=villager)
        return render(request, 'nooklist/villager_form.html'{'form': form})


def resources_edit(request, pk):
    resources = Resources.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResourcesForm(request.POST, instance=resources)
        if form.is_valid():
            resources = form.save()
            return redirect('resources_detail', pk=resources.pk)
        else:
            form = ResourcesForm(instance=resources)
        return render(request, 'nooklist/resources_form.html'{'form': form})


def recipes_edit(request, pk):
    recipes = Recipes.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipesForm(request.POST, instance=recipes)
        if form.is_valid():
            recipes = form.save()
            return redirect('recipes_detail', pk=recipes.pk)
        else:
            form = RecipesForm(instance=houseware)
        return render(request, 'nooklist/recipes_form.html'{'form': form})

def recipes_delete(request, pk):
    Recipes.objects.get(id=pk).delete()
    return redirect('recipes_list')


def resources_delete(request, pk):
    Resources.objects.get(id=pk).delete()
    return redirect('resources_list')


def clothing_delete(request, pk):
    Clothing.objects.get(id=pk).delete()
    return redirect('clothing_list')


def villager_delete(request, pk):
    Villager.objects.get(id=pk).delete()
    return redirect('villager_list')


def clothing_delete(request, pk):
    Clothing.objects.get(id=pk).delete()
    return redirect('clothing_list')



class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode(
            {'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})