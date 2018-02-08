from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return "app02 %s " % self.name

    class Meta:
        app_label = "app02"