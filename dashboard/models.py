from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Candidates(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	birth_date = models.DateField()
	nationality = CountryField()
	LEVELS = (
		('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
		('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),	('10', '10'),
	)
	level_of_english = models.CharField(max_length=2, choices=LEVELS, blank=True)
	note = models.TextField(blank=True)
	resume = models.FileField(upload_to='resumes', blank=True)
        def __unicode__(self):
            return self.first_name + ' ' + self.last_name