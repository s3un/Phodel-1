
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
	first_name= models.CharField(max_length=20, default='Name')
	last_name = models.CharField(max_length=20, default='Name')
	tag = models.CharField(max_length=10, default='Model')
	gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=True)
	height = models.PositiveIntegerField(blank=True, null=True)
	email = models.EmailField()
	career_summary = models.TextField(blank=True)
	weight = models.CharField(max_length=50, blank=True)
	skin_color=models.CharField(max_length=50, blank=True)
	age = models.PositiveIntegerField(blank=True, default=1)
	model_image = models.ImageField(upload_to="Users/Model", default='Users/Model/user.png', blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.user.username
		
	def __unicode__(self):
		return "first_name: {}" .format(self.first_name)

class Pcompany(models.Model):
	user = models.OneToOneField('CustomUser',on_delete=models.CASCADE)
	tag= models.CharField(max_length=10, default='Seeker')
	company_name= models.CharField(max_length=50)
	address = models.TextField()
	contact_number = models.CharField(max_length=50, blank=True)
	email  = models.EmailField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.user.username

class images(models.Model):
	User = models.ForeignKey('Pmodel', on_delete="CASCADE")
	image = models.ImageField(upload_to="'Users'+User", blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.User.first_name

class interest(models.Model):
	Users=models.ForeignKey('Pmodel', on_delete=models.CASCADE)
	interests = models.CharField(max_length=50, blank=True)
	def publish(self):
		self.save()

	def __str__(self):
		return self.User.first_name +' '+ self.interests