from django.db import models
from .Raw_product import Raw_Product


class RM_provider(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Raw_type = models.ForeignKey(Raw_Product, on_delete=models.CASCADE)
    password = models.CharField(max_length=500)
    location = models.CharField(max_length=100, default='Select')

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return RM_provider.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if RM_provider.objects.filter(email=self.email):
            return True

        return False

    class Meta:
        db_table = "RM_provider_Login"
