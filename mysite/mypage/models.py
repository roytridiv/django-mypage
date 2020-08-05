from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 11)
    password = models.CharField(max_length = 11)
    date_time = models.DateTimeField(blank=True)

    def __str__(self):
        template = '{0.name}`~`{0.email}`~`{0.phone}`~`{0.password}'
        return template.format(self)
