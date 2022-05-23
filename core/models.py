from django.db import models

# Create your models here.

class Icons(models.Model):
    icons = models.CharField(max_length=100)

    class Meta:
        db_table = 'icons'

    def __str__(self):
        return self.icons      #obriga o admin do django a apresentar os icons pelo nome