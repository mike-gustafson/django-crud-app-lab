from django.contrib import admin
from .models import System, Game, Accessory

# Register your models here.
admin.site.register(System)
admin.site.register(Game)
admin.site.register(Accessory)
