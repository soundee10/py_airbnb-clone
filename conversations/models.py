from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Conversation model Definition"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = ForeignKey("users.User", on_delete=models.CASCADE)
    Conversation = ForeignKey("Conversation", on_delete=CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
