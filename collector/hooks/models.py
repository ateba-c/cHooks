from django.db import models

# Create your models here.
class signals(models.Model):
    #signal_id=models.AutoField(primary_key=True)
    ticker=models.CharField(max_length=10)
    updated = models.CharField(max_length=20)
    quote = models.CharField(max_length=20)
    strategy = models.CharField(max_length=20)
