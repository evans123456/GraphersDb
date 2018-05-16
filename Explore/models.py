from django.db import models
from django.urls import reverse


# Create your models here.
class Users(models.Model): #songs (buuuut in buckys this is the equivalent of albums)
	username = models.CharField(max_length=250)
	profile_picture = models.FileField()
	Location = models.CharField(max_length=250)
	links = models.CharField(max_length=250)
	contacts = models.CharField(max_length=250)
	charges = models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse("music:detail",kwargs = {"pk":self.pk})

	def __str__(self):
		return self.username + '-->' + self.Location


class Pictures(models.Model): #albums
	photographer = models.ForeignKey(Users , on_delete= models.CASCADE)
	category = models.CharField(max_length=250)
	post = models.FileField()
	post_title = models.CharField(max_length=250)

	def __str__(self):
		return self.category + '-->' + self.post_title
 