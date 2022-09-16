from django import forms
from .models import Houseware, Recipes, Resources, Clothing, Villager

class HousewareForm(forms.ModelForm):

    class Meta:
        model = Houseware
        fields =('name', 'descripition', 'bid price', 'photo',)

class RecipesForm(forms.ModelForm):

    class Meta:
        model = Recipes
        fields =('name', 'descripition', 'bid price', 'photo',)

class ResourcesForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields =('name', 'descripition', 'bid price', 'photo',)

class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields =('name', 'descripition', 'bid price', 'photo',)

class VillagerForm(forms.ModelForm):

    class Meta:
        model = Villager
        fields =('name', 'descripition', 'bid price', 'photo',)

class ThreadForm(forms.Form):

    username = forms.CharField(label ='', max_length=100)

class MessageForm(forms.ModelForm):

    body = forms.CharField(label='', max_length=1000)

    image = forms.ImageField(label='Send an image', required=False)

    class Meta:
        model = MessageModel

        fields = ('body', 'image')
