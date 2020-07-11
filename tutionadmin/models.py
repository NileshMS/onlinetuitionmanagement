from django.db import models

# Create your models here.
class AddCourse(models.Model):
    courseid= models.AutoField(primary_key=True)
    course = models.CharField(max_length=60)
    faculty = models.CharField(max_length=50)
    date =models.DateField()
    time = models.CharField(max_length=20)
    fee = models.IntegerField()
    duration = models.CharField(max_length=20)


    def __str__(self):
        return self.course

class MainAdminRegister(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username