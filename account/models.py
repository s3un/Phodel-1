
# from Jobs.models import Gender
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
from django.db import models

class Gender(models.Model):
	"""
	Description: Model Description
	"""
	gender= models.CharField(max_length=10)
	tags= models.CharField(max_length=1)	
	def publish(self):
		self.save()

	def __str__(self):
		return self.gender

class CustomUserManager(UserManager):
	pass

class CustomUser(AbstractUser):
	# objects= CustomUserManager()
	is_model= models.BooleanField(default=False)
	is_company = models.BooleanField(default=False)

class Pmodel(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=True)
	height = models.CharField(max_length=50, blank=True)
	email = models.EmailField()
	career_summary = models.TextField(blank=True)
	weight = models.CharField(max_length=50, blank=True)
	eye_color=models.CharField(max_length=50, blank=True)
	age = models.PositiveIntegerField(blank=True, default=1)
	model_image = models.ImageField(upload_to="Users/Model")

	def publish(self):
		self.save()

	def __str__(self):
		return self.user.username

class Pcompany(models.Model):
	user = models.OneToOneField('CustomUser',on_delete=models.CASCADE)
	company_name= models.CharField(max_length=50)
	address = models.TextField()
	contact_number = models.CharField(max_length=50)
	email  = models.EmailField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.user.username






