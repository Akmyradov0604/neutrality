from django.db import models
from neutrality.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Turkmen(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	date = models.DateField(auto_now=True)
	slug = models.SlugField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:200]
def slug_generator(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Turkmen)