from django.db import models

# Create your models here.
class Speaker(models.Model):
    speaker_name=models.CharField(max_length=100)
    speaker_company=models.CharField(max_length=100)
    speaker_position=models.CharField(max_length=100)
    speaker_date=models.DateField()
    speaker_image=models.ImageField(upload_to='images/', blank=True)