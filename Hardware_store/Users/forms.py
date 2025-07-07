from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.defaultfilters import first

from . import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username','email', 'first_name', 'last_name']