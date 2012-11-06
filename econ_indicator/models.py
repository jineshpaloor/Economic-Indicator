from django.db import models

class History(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    year = models.CharField(max_length=1, choices=[(year,year) for year in range(2000,2013)])
    month = models.CharField(max_length=1, choices=[(month,month) for month in range(1,13)])
    nominal = models.CharField(max_length=100)

class EconomicIndicator(models.Model):
    Periods = (
                ('yearly', 'Yearly'),
                ('quarterly', 'Quarterly'),
                ('monthly', 'Monthly'),
                ('weekly', 'Weekly'),
                ('biweekly', 'BiWeekly'),
                ('daily', 'Daily'),
            )
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    publish_period = models.CharField(max_length=1, choices=Periods)
    parent_id = models.IntegerField(default=0)
    history = models.ForeignKey(History)


