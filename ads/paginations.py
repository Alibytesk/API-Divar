from rest_framework.pagination import PageNumberPagination
from accounts.models import User


class StandardResultSetPagination(PageNumberPagination):
    page_size = getattr(User, 'PAGINATION_PAGE_SIZE', 1)
