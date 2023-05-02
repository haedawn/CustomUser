from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from.models import CustomUser

class CustomUserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        Fields = ['username']

class CustomUserSigninForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        Fields = ['username']