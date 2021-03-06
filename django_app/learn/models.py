from uuid import uuid4
from django.db import models

# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    draft = models.BooleanField(default=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)


class LessonItem(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)

    class Meta:
        abstract = True


# We use learning and native here to make this a bit more generic, though
# We don't specify the languages in question yet.
# For our purposes, learning = English and native = Spanish
class Vocabulary(LessonItem):
    learning = models.CharField(max_length=255)
    native = models.CharField(max_length=255)
    audio = models.FileField(upload_to="vocabulary/", null=True)

