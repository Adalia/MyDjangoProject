# -*- coding: utf-8 -*-

from django.http import HttpResponse

from model.models import Test


# 数据库操作
def testdb(request):
    Test(name='hahahhaha').save()
    return HttpResponse("<p>数据添加成功！</p>")