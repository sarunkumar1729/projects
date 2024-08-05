from django.db import models
from django.contrib.auth.models import User

class Jobs(models.Model):
      title = models.CharField( max_length=100)
      skills = models.CharField(max_length=100,null=True)
      location = models.CharField(max_length=100)
      category = models.CharField(max_length=100,null=True)
      job_type = models.CharField(max_length=100,null=True)
      gender = models.CharField(max_length=100,null=True)
      min_age = models.IntegerField(null=True)
      max_age = models.IntegerField(null=True)
      qualification = models.CharField(max_length=100)
      experience = models.IntegerField()
      min_salary = models.CharField(max_length=100)
      max_salary = models.CharField(max_length=100)
      vacancy = models.IntegerField(null=True)
      updated_at = models.DateField(auto_now=True,null=True)
      def __str__(self):
            return(self.title)
      
class Profile(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      address = models.CharField(max_length=100)
      phone1 = models.CharField(max_length=100)
      phone2 = models.CharField(max_length=100)
      age = models.IntegerField()
      employed = models.BooleanField()
      skills = models.CharField(max_length=100)
      qualification = models.CharField(max_length=100)
      certifications = models.CharField(max_length=100)
      resume = models.FileField(upload_to='resume', max_length=100)
      about = models.CharField(max_length=100)
      user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      
class JobApplications(models.Model):
      user = models.ForeignKey(User, on_delete = models.CASCADE)
      job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
      applied_date = models.DateTimeField( auto_now=True)
      status = models.CharField(max_length = 100 , default='pending')
      
class Notifications(models.Model):
      msg = models.CharField(max_length=255)
      description = models.CharField(max_length=255)
      date = models.DateField(auto_now=True)
      read = models.BooleanField(default=False)
      
class Messages(models.Model):
      message = models.CharField(max_length=255)
      full_name = models.CharField(max_length=255,null=True)
      email = models.CharField(max_length=255,null=True)
      subject = models.CharField(max_length=255,null=True)
      send_date = models.DateField(auto_now=True)