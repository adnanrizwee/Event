from django.db import models
from datetime import datetime
from django.utils.timezone import now

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
# Create your models here.
class Eventer(models.Model):
    # class StateChoice(models.TextChoices):
    #     Alabama = 'Alabama, AK'
    #     Alaska = 'Alaska, AZ'
    #     Arkansas = 'Arkansas, CA'
    title = models.CharField(max_length= 50)
    place = models.CharField(max_length= 50)
    city = models.CharField(max_length= 10)
    gender = models.CharField(max_length= 50, choices=GENDER_CHOICES)

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self):
        return self.title



