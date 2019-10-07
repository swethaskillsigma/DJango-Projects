from django.db import models

# Create your models here.
class Stud(models.Model):
    stud_name=models.CharField(max_length=30)
    stud_course=models.CharField(max_length=30)
    class Meta:
        db_table="stud"
        #table gets created automatically on migration


# then apply the following in command prompt
# python manage.py migrate --run-syncdb
# python manage.py makemigrations
# python manage.py migrate
# check the database for new table in database if its mysql