from django import forms
from .models import System, Game, Accessory

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'manufacturer', 'release_year']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'release_year']

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'description'] 