from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wallpaper, Comment, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class WallpaperForm(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ["title", "img", "category", "screen_type"]
        labels = {
            'title': 'Título',
            'img': 'Imagen',
            'category': 'Categoría',
            'screen_type': 'Tipo de pantalla',
        }

class WallpaperUpdateForm(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ["title", "img", "category", "screen_type"]
        labels = {
            'title': 'Título',
            'img': 'Imagen',
            'category': 'Categoría',
            'screen_type': 'Tipo de pantalla',
        }
    
    def __init__(self, *args, **kwargs):
        super(WallpaperUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar'))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {'name': 'Nombre de la categoria'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {'text': 'Escribe un comentario'}