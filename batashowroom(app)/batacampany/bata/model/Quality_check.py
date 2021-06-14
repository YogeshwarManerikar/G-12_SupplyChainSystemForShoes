from django.db import models


class Quality_checking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    location = models.CharField(max_length=100,default='Select')
    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return Quality_checking.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Quality_checking.objects.filter(email=self.email):
            return True

        return False


    class Meta:
        db_table = "Quality_checking_LOGIN"
