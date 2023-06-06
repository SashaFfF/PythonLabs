from django import forms
from  .models import *
from django.contrib.auth.forms import AuthenticationForm

class AddDealForm(forms.ModelForm):
    def __input__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Owner'].empty_label = "Владелец не выбран"
    class Meta:
        model=Deal
        fields = '__all__'

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
