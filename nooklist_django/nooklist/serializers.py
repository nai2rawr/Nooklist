from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()
from .models import Houseware, Recipes, Resources, Villager, Clothing

class VillagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villager
        fields = ('name', 'description', 'bid_price', 'photo')


class ClothingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothing
        fields = ('name', 'description', 'bid_price', 'photo')


class HousewareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Houseware
        fields = ('name', 'description', 'bid_price', 'photo')


class ResourcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resources
        fields = ('name', 'description', 'bid_price', 'photo')


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('name', 'description', 'bid_price', 'photo')

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
