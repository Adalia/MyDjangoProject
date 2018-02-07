from django.db import models

# Create your models here.
class Test(models.Model):  #类名为数据库表名，表名组成结构为：应用名_类名（如：model_test）。
    name = models.CharField(max_length=20)