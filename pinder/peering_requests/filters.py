from rest_framework import filters

from .models import Request


class RequestFilterSet(filters.FilterSet):

    class Meta(object):
        model = Request
        fields = [
            "id",
            "sender",
            "receiver",
            "state",
            "sender_is_ready",
            "receiver_is_ready",
            "created",
            "modified"
        ]
