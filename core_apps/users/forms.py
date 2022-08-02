from django.contrib.auth import forms as admin_forms

from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _


User = get_user_model()

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm):
        model = User
        fields = "__all__"

class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm):
        model = User
        fields = "__all__"
        error_messages = {
            "username": {
                "unique":_("This username has already taken"),
            },
        }