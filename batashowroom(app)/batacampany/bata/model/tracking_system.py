from django.db import models


class Tracking_reports(models.Model):
    tracking_id= models.IntegerField()
    date = models.DateField(default=None)
    track_status = models.CharField(max_length=999)


    class Meta:
        db_table = "Tracking_reports"
