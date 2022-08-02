from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = UserCreationForm
    form = UserChangeForm
    moedl = User
    list_display = ["pkid", "id", "email", "username", "first_name", "last_name", "is_staff", "is_active",]
    list_display_links = ["id", "email"]
    list_filter = ["email", "username", "first_name", "last_name", "last_name", "is_staff"]
    fields_sets = (
        (
            _("Login Credentials"),
            {
                "fields":(
                    "email",
                    "password",
                )
            },
        ),
        (
            _("personal_information"),
            {
                "fields": ("username", "first_name", "lastname",),
            },
        ),
        (
            _("permissions_and_goups"),
            {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),
            },
        ),
        (
          _("Important_dates"),
          {
            "fields":("last_login", "created_at",),
          },  
        ),
    )
    add_fieldsets = (
        (
          None,
          {
            "classes":("wide",),
            "fields":("email","password1", "password2", "is_staff", "is_active",),
          } , 
        ),
    )
    search_fields = ["email", "username", "first_name", "last_name",]

admin.site.register(User, UserAdmin)
