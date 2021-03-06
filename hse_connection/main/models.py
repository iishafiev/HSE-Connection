from django.db import models
from django.contrib.auth.models import User

'''
Stores user information
'''
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
	position = models.CharField(max_length=250)
	avatar = models.ImageField(upload_to='user_avatars')
	campus = models.CharField(max_length=100)
	faculty = models.CharField(max_length=250)


'''
Represents the publication
'''
class Publication(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length=250)
	text = models.TextField()
	date = models.DateTimeField()