"""
Definition of models.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Country(models.Model):
    country_name = models.CharField(max_length=32)
    pub_date = models.DateTimeField('Data publikacji')
    def __str__(self):
        return self.country_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.short_description = 'Ostatnio opublikowane'

@python_2_unicode_compatible
class Shop(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=32)
    def __str__(self):
        return self.shop_name

    