from django.contrib.auth.forms import (
    UserCreationForm as AuthUserCreationForm,
    UserChangeForm as AuthUserChangeForm,
)

from .models import User


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User
