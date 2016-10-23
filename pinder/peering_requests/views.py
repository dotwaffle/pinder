from django.views.generic import DetailView, ListView

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Request
from .serializers import RequestSerializer, PostRequestSerializer
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
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_class = RequestFilterSet
    ordering_fields = ("sender", "receiver", "created", "modified")
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return PostRequestSerializer
        return RequestSerializer


class RequestListView(ListView):
    model = Request
    template_name = "peering_requests/listing.html"


class RequestDetailView(DetailView):
    model = Request
    template_name = "peering_requests/detail.html"


class RequestAcceptanceView(DetailView):
    model = Request
    template_name = "peering_requests/acceptance.html"
