from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=1)
    price = models.FloatField()
    special_price = models.FloatField(default=0)

    def __unicode__(self):
        return self.title
