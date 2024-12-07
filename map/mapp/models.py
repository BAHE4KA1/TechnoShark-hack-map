from django.db import models

"""
class Routes(models.Model):
    name = models.CharField(max_length=100)
    dot_start = models.CharField(max_length=20)
    dot_end = models.CharField(max_length=20)
    trip_time = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Drivers(models.Model):
    marks = [
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        ('4', 'FOUR'),
        ('5', 'FIVE'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    freelance = models.BooleanField()
    rating = models.CharField(max_length=20, choices=marks, default='5')

    def __str__(self):
        return self.first_name+' '+self.last_name
"""


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
    if traffic_value in ['1', '2', '3', '4']: traffic_color = '#22A819'
    elif traffic_value in ['5', '6', '7']: traffic_color = '#FFCC00'
    else: traffic_color = '#E8413E'

    time_start = models.CharField(max_length=20, default=None)
    time_end = models.CharField(max_length=20, default=None)

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