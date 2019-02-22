from django.db import models

# Create your models here.

class News(models.Model):
	Title = models.CharField(max_length=50)
	TextField = models.TextField()
	TimePublished = models.DateTimeField()
	DatePublished = models.DateField()
	def __str__(self):
		return self.Title
	

class Comment(models.Model):
	Name = models.CharField(max_length=50)
	TextField = models.TextField()
	News_Id = models.ForeignKey('News', on_delete=models.CASCADE, default=3)
	def __str__(self):
		return self.Name
	
		
	
	