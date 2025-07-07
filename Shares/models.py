from django.db import models

# Create your models here.


class Shares(models.Model):
    name = models.CharField(max_length=128, blank = False, verbose_name='shares-name')
    description = models.CharField(max_length=256, blank = False, verbose_name='shares-description')
    date_before = models.DateTimeField(blank= True ,verbose_name='date-before')
    views = models.IntegerField(default=0, verbose_name="count-of-view")

    STATUS_CHOICES = [
        ('СКИДКИ', 'СКИДКИ'),
        ('РАСПРОДАЖА', 'РАСПРОДАЖА'),
        ('ВЫГОДА', 'ВЫГОДА'),
        ('НОВИНКИ', 'НОВИНКИ'),
        ('СЕЗОННЫЕ', 'СЕЗОННЫЕ'),
    ]

    status = models.CharField(choices=STATUS_CHOICES,verbose_name="articl-shares",default='BENEFIT')

    class Meta:
        db_table = "Акции компании"

    def __str__(self):
        return self.name

