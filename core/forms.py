from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')], required=True)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'user_type')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with that email already exists.')
        return username


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
        