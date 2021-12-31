from django.db import models

class APS(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}--{self.name}--{self.description}"

