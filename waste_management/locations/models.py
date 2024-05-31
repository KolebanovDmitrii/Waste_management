# locations/models.py
from django.db import models

class WasteDisposalLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
