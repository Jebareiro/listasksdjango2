from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age', 'password1', 'password2')  # Ahora 'username' es necesario

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',  # 'username' ya no es parte del modelo CustomUser
            'age',    # 'age' sí es parte del modelo
        )
