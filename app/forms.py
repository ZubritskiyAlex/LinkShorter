from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import URL


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ['current_url']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'first_name', 'last_name', 'email']
