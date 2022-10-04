from django.contrib import admin
from .models import Resources, Recipes, Villager, Clothing, Houseware

# Register your models here.
admin.site.register(Recipes)
admin.site.register(Resources)
admin.site.register(Houseware)
admin.site.register(Clothing)
admin.site.register(Villager)
