from django import forms
from .models import Board, Favorite


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "content", "name"]


class FavoriteFrom(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ["board"]
