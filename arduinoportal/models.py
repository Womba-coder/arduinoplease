from django.db import models

# Create your models here.
class Info(models.Model):
    data = models.CharField(max_length=100)
    timeStp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.data 
