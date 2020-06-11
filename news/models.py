from django.db import models

from ckeditor.fields import RichTextField

class News(models.Model):
	title = models.CharField(max_length=200)
	body = RichTextField()
	date = models.DateField(auto_now=True)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:200]