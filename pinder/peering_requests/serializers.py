from rest_framework import serializers

from users.serializers import IspSerializer, UserSerializer

from .models import Request


class RequestSerializer(serializers.ModelSerializer):

    sender = UserSerializer(read_only=True)
    receiver = IspSerializer(read_only=True)

    class Meta(object):
        model = Request
        fields = (
            "id",
            "sender",
            "receiver",
            "ixlan_id",
            "state",
            "sender_is_ready",
            "receiver_is_ready",
            "created",
            "modified"
        )


class PostRequestSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Request
        fields = (
            "id",
            "sender",
            "receiver",
        )
