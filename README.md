#### MyDjangoProject
##### 该项目是初次接触Django建立的项目，里面主要尝试了不同的app使用不同数据库的操作

多数据库操作参考博客：http://blog.csdn.net/songfreeman/article/details/70229839

启动项目：
    python manage.py runserver 0.0.0.0:8000
    
创建项目：django-admin.exe startproject  projectname

创建app：django-admin.py startapp appname


模型修改：
1.现在模型里修改;
2.python manage.py makemigrations appname  # 让 Django 知道我们在我们的模型有一些变更;
3.python manage.py migrate --database=db02  # 创建表结构;


python==3.6
Django==2.0.2
PyMySQL==0.8.0
