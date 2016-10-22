from rest_framework import serializers

from .models import Isp, User


class IspSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Isp
        fields = ("name", "asn")


class UserSerializer(serializers.ModelSerializer):

    isp = IspSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("name", "email", "isp")
