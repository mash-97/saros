from django.db import models


class SarosLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.timestamp}: {self.message}"

