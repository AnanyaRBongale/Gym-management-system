from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models 
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    description=models.TextField()

    def __str__(self):
        return self.email
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id
    def __str__(self):
        #x=str
        return self.plan+" - "+str(self.price)

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.ForeignKey(MembershipPlan,on_delete=models.CASCADE)
    SelectTrainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    Address=models.TextField()
    
    def __str__(self):
        return self.FullName





class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True)
    def __int__(self):
        return self.id

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id   