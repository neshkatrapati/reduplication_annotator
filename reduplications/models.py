# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ReduplicationCategory(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


# class ReduplicationTypeManager(models.Manager):
# 	def as_choices(self):
# 		for rtype in self.all():
# 			yield (rtype.pk, force_text(rtype))


class ReduplicationType(models.Model):
	#objects = ReduplicationTypeManager()
	name = models.CharField(max_length=200)
	description = models.TextField()
	def __str__(self):
		return self.name


class Reduplication(models.Model):
	token = models.CharField(max_length=2000)
	frequency = models.IntegerField(default = 0)
	category  = models.ForeignKey(ReduplicationCategory, null = True)
	examples = models.TextField() # Example Sentences
	#types = models.CharField(max_length=2000, null = True)
	types = models.ManyToManyField(ReduplicationType)
	change_date = models.DateTimeField('date changed')


	def __str__(self):
		return self.token.encode('utf-8')