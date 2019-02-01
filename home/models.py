from django.db import models

# Create your models here.

class Phodel(models.Model):
	name = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	Contact_info = models.CharField(max_length=50)
	Email = models.EmailField()
	logo = models.ImageField(upload_to='company/logo')
	Facebook = models.URLField()
	Twitter = models.URLField()
	Instagram = models.URLField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.name
