from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserSignupForm(ModelForm):
    class Meta:
        fields = ('first_name','last_name','username','email','password')
        model = User

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
