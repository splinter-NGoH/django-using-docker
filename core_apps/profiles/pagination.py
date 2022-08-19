from prometheus_client import pushadd_to_gateway
from rest_framework.pagination import PageNumberPagination


class ProfilePagination(PageNumberPagination):
    page_size = 3
