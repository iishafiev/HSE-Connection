from django.db import models
from django.contrib.auth.models import User

'''
Stores user information
'''
class UserProfile(models.Model):
	CAMPUS_CHOICES = [
		('Msc','Moscow'),
		('Spb','Saint-Petersburg'),
		('NNvgd','Nizhny Novgorod'),
		('Perm','Perm')
	]

	email = models.EmailField()
	position = models.CharField(max_length=250)
	avatar = models.ImageField()
	campus = models.CharField(choices=CAMPUS_CHOICES, max_length=100)


'''
Represents the publication
'''
class Publication(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length=250)
	text = models.TextField()
	date = models.DateTimeField()