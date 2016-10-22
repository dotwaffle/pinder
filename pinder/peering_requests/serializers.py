from rest_framework import serializers

from .models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Request
        fields = (
            "id",
            "sender",
            "receiver",
            "state",
            "sender_is_ready",
            "receiver_is_ready",
            "created",
            "modified"
        )


class PostRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Request
        fields = (
            "id",
            "sender",
            "receiver",
        )
