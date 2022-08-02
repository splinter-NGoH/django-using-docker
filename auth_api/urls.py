from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        description="Auth api",
        default_version="v1",
        contact=openapi.Contact(email="ahmedmansy265@gmail.com"),
        license=openapi.License(name="MIT license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc"
    ),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header= "Auth API"
admin.site.site_title = "Auth API"
admin.site.index_title = "Welcome to the Auth Site"