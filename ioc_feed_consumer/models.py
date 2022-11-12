from django.db import models

class IndicatorType(models.TextChoices):
    IP = "IP"
    Hash = "Hash"
    Domain = "Domain"
    URL = "URL"
    File = "File"

# Create your models here.
class Ioc(models.Model):
    ioc = models.TextField(primary_key=True)
    type = models.TextField(choices=IndicatorType.choices)
    sources = models.JSONField()
    frequency = models.IntegerField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    location = models.JSONField(null=True)

    # string representation of the model
    def __str__(self):
        return f"Ioc: {self.ioc} | Type: {self.type} | Source: {self.sources} | Frequency: {self.frequency} | Created At: {self.created_timestamp} | Updated At: {self.updated_timestamp} | Location: {self.location}"  