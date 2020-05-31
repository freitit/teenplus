from django import forms
from .models_from_db import Entity
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class EntityForm(forms.Form):
    # entity_id = forms.IntegerField(required=False)
    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    created_date = forms.DateField(required=False)
    user_id = forms.IntegerField(required=False)
    theme = forms.CharField(max_length=255)

    # class Meta:
    #     model = Entity  
    #     fields = "__all__"

class AuthenForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'input','placeholder': 'Tên đăng nhập'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'input','placeholder':'Mật khẩu'}))