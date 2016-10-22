from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Isp, User
from .serializers import IspSerializer, UserSerializer


class IspViewSet(ModelViewSet):
    model = Isp
    queryset = Isp.objects.all()
    serializer_class = IspSerializer
    permission_classes = (AllowAny,)


class UserViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        login(self.request, User.objects.get(pk=2))
        return reverse("index")
