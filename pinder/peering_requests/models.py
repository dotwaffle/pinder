from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):

    STATE_WAITING = "waiting"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    STATES = (
        (STATE_WAITING, "Waiting"),
        (STATE_ACCEPTED, "Accepted"),
        (STATE_REJECTED, "Rejected"),
    )

    sender = models.ForeignKey(User, related_name="requests_received")
    receiver = models.ForeignKey(User, related_name="requests_sent")

    state = models.CharField(
        choices=STATES, default=STATE_WAITING, max_length=8)

    sender_is_ready = models.BooleanField(default=False)
    receiver_is_ready = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
