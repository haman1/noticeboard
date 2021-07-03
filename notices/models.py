from django.db import models
from django.utils import timezone

# Create your models here.


class Notice(models.Model):
    noticetitle = models.CharField(max_length=20)
    noticedesc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.noticetitle, self.id)


