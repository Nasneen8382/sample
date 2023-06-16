from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.IntegerField()

class TeacherModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=200)
    Phone=models.IntegerField()
    Image = models.ImageField(upload_to="image/", null=True)

class StudentModel(models.Model):
    std_course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    std_fname=models.CharField(max_length=200)
    std_lname = models.CharField(max_length=200)
    std_email=models.CharField(max_length=25)
    std_phone=models.IntegerField()
    std_address=models.CharField(max_length=25)
    # std_image = models.ImageField(upload_to="image/", null=True)