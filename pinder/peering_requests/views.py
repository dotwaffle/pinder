from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Request
from .serializers import RequestSerializer
from .filters import RequestFilterSet


class StandardPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page-size"
    max_page_size = 100000


class RequestViewSet(ModelViewSet):
    model = Request
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    pagination_class = StandardPagination
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = RequestFilterSet
    ordering_fields = ("sender", "receiver", "created", "modified")
