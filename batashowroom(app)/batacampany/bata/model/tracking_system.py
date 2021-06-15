from django.db import models


class Tracking_reports(models.Model):
    date = models.DateField(default=None)
    track_status = models.CharField(max_length=999)
