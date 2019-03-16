from django.db import models
from django.utils import timezone
# Create your models here.

class States(models.Model):
	"""
	Description: Model Description
	"""
	state= models.CharField(max_length=50)
	def publish(self):
		self.save() 

	def __str__(self):
		return self.state

class Lga(models.Model):
	lga = models.CharField(max_length=50, null=True)
	state = models.ForeignKey(States, on_delete=models.DO_NOTHING, null=True)
	def publish(self):
		self.save()

	def __str__(self):
		return self.lga

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

class Job(models.Model):
	Job_title = models.CharField( max_length=50)
	Job_author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, default=True)
	state= models.ForeignKey('States', on_delete=models.CASCADE)
	lga = models.ForeignKey(Lga, on_delete=models.CASCADE, default=True)
	town = models.CharField(max_length=50, default=' ')
	street_address = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	gender= models.ManyToManyField('Gender')
	height = models.PositiveIntegerField(blank=True)
	Job_Description = models.CharField(max_length=200, default=' ')
	personal_note= models.CharField(max_length=500, blank=True)
	payout = models.FloatField(default=1.0)
	jslug=models.SlugField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.Job_title

class Featured_Jobs(models.Model):
	jobs=models.ForeignKey('Job', on_delete=models.CASCADE, default=1)

	def publish(self):
		self.save()

	def __str__(self):
		return self.jobs.Job_title

class Hot_Jobs(models.Model):
	jobs=models.ForeignKey('Job', on_delete=models.CASCADE, default=1)

	def publish(self):
		self.save()

	def __str__(self):
		return self.jobs.Job_title

class Application(models.Model):
	Job_title= models.CharField(max_length=50, blank=True)
	job_id = models.PositiveIntegerField(default=1)
	Job_author=models.CharField(max_length=50, blank=True)
	applicant= models.CharField(max_length=100, blank=True)
	applicant_mail= models.EmailField(blank=True)
	applicant_id = models.PositiveIntegerField()
	author_id = models.PositiveIntegerField(default=1)
	status = models.PositiveIntegerField(default=0)

	def publish(self):
		self.save()

	def __str__(self):
		return self.applicant + ' '+self.Job_title

class Offer(models.Model):
	job =models.ForeignKey('Job', on_delete=models.CASCADE)
	applicant= models.CharField(max_length=100, blank=True)
	applicant_mail= models.EmailField(blank=True)
	applicant_id = models.PositiveIntegerField()
	author_id = models.PositiveIntegerField(default=1)
	status = models.PositiveIntegerField(default=0)

	def publish(self):
		self.save()

	def __str__(self):
		return self.applicant + ' '+self.job.Job_title