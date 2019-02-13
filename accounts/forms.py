from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_image','user_bio')
#         #Well add post forms here later too!
#


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
