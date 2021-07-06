from django.db import models


class Tracking_reports(models.Model):
    tracking_id = models.IntegerField()
    date = models.DateField(default=None)
    track_status = models.CharField(max_length=999)

    @staticmethod
    def get_track_status(tracking_id):
        try:
            return Tracking_reports.objects.get(tracking_id=tracking_id)
        except:
            return False

    class Meta:
        db_table = "Tracking_reports"
