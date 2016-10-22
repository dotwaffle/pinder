import django_filters

from .models import Request


class RequestFilterSet(django_filters.FilterSet):

    class Meta:
        model = Request
        fields = (
            "state",
            "sender_is_ready",
            "receiver_is_ready",
            "ixlan_id"
        )
