from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pkid","id",'user', 'phone_number',"gender")
    list_filter = ('country', 'city', 'gender')
    search_fields = ('phone_number',  'country', 'city',  )
    ordering = ('id', "pkid")

admin.site.register(Profile, ProfileAdmin)