from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField
from taggit.managers import TaggableManager

class Sower(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=40, default="You need a title")
	description = models.CharField(max_length=1000)
	address = models.CharField(max_length=1000, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	website = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	#logo = models.ImageField(upload_to="logo/")
	rating = RatingField(range=5)

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	text = models.CharField(max_length=40)

	def __unicode__(self):
		return self.text

class Grower(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=40)
	skills = models.ManyToManyField(Tag, related_name='skills_growers', blank=True)
	#avatar = models.ImageField(upload_to="avatar/")
	interests = models.ManyToManyField(Tag, related_name='interests_growers', blank=True)

	rating = RatingField(range=5)

	def __unicode__(self):
		return repr(self.user)

class Task(models.Model):
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
	address = models.CharField(max_length=1000, null=True, blank=True)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.title

