from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from peering_requests.views import RequestViewSet

from .views import IndexView


router = DefaultRouter()
router.register(r'requests', RequestViewSet)

urlpatterns = [
    url(
        r"^api/auth/",
        include('rest_framework.urls', namespace="rest_framework")
    ),
    url(r"^api/", include(router.urls, namespace="drf")),
    url(r"^$", IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
]
