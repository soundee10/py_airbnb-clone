from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Conversation model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = ForeignKey("users.User", on_delete=models.CASCADE)
    Conversation = ForeignKey(
        "Conversation", related_name="messages", on_delete=CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
