from django.db import models
from .neuro import *

class Streets(models.Model):
    t_marks = [
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        ('4', 'FOUR'),
        ('5', 'FIVE'),
        ('6', 'SIX'),
        ('7', 'SEVEN'),
        ('8', 'EIGHT'),
        ('9', 'NINE'),
        ('10', 'TEN'),
    ]

    name = models.CharField(max_length=100, default='Красная')
    traffic_value = models.CharField(max_length=20, choices=t_marks, default='1')
    traffic_color = models.CharField(max_length=20, default='#FFFFFF')

    time_start = models.CharField(max_length=20, default=None)
    time_end = models.CharField(max_length=20, default='1')

    def save(self, *args, **kwargs):
        if int(self.traffic_value) < 4: self.traffic_color = '#22A819'
        elif int(self.traffic_value) < 8: self.traffic_color = '#FFCC00'
        else: '#E8413E'

        self.time_end = n.answer(str(self.time_start)+' '+str(self.traffic_value))
        super(Streets, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Log(models.Model):
    actions = [
        ('Изменение задержки светофора',  'DURATION_CHANGE'),
        ('Заупск мигающего режима', 'ACCIDENT_MODE'),
        ('Другое', 'OTHER')
    ]

    log_date_time = models.DateTimeField()
    action = models.CharField(max_length=100, choices=actions)
    actor = models.CharField(max_length=100)

    def __str__(self):
        return self.actor
