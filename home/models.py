from django.db import models

# Create your models here.
class payment(models.Model):
    user = models.CharField(max_length=100)
    amount = models.IntegerField(default=100)
    
    
    def __str__(self):
        return self.user