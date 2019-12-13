from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Boardtbl(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    insert_date = models.DateTimeField(default=timezone.now)
    insert_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
