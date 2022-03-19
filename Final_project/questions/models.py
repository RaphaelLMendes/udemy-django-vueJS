from django.conf import settings
from django.db import models
import uuid as uuid_lib
from django.conf import settings
from core.models import TimestampedModel

class Question(TimestampedModel):
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return self.content

class Answer(TimestampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers"
    )
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")

    def __str__(self):
        return self.author.username
