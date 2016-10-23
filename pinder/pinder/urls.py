from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from peering_requests.views import (
    RequestViewSet, RequestDetailView, RequestAcceptanceView, RequestListView)
from users.views import LoginView

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

    url(r"^requests/$", RequestListView.as_view(), name="request-list"),
    url(
        r"^requests/(?P<pk>\d+)",
        RequestAcceptanceView.as_view(),
        name="request-detail"
    ),
    url(
        r"^requests/(?P<pk>\d+)/acceptance/",
        RequestDetailView.as_view(),
        name="request-acceptance"
    ),

    url(r"^hacks/login", LoginView.as_view(), name="login-hack"),
    url(r'^admin/', admin.site.urls),

]
