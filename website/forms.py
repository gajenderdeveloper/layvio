from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# from .models import User

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
            max_length=100,
            required = True,
            help_text='Enter Email Address',
            widget=forms.TextInput(attrs={'class': 'input100'}),
            )
    password1 = forms.CharField(
            max_length=100,
            required = True,
            help_text='Enter Password',
            widget=forms.PasswordInput(attrs={'class': 'input100'}),
            )
    password2 = forms.CharField(
            max_length=100,
            required = True,
            help_text='Enter Password',
            widget=forms.PasswordInput(attrs={'class': 'input100'}),
            )
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(
            max_length=100,
            required = True,
            help_text='Enter Email Address',
            widget=forms.TextInput(attrs={'class': 'input100'}),
            )
    password = forms.CharField(
            max_length=100,
            required = True,
            help_text='Enter Password',
            widget=forms.PasswordInput(attrs={'class': 'input100'}),
            )
    class Meta:
        model = User
        fields = ('email', 'password')