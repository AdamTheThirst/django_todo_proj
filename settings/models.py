from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    '''Time stamps base template'''

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(f'{self.pk} — {self.created}')