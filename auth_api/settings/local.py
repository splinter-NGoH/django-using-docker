from .base import *

from .base import env


DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default="ASADFSDAasdfadfASDFASFSADASDF",)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
