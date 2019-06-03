from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=20)
	role = models.CharField(max_length=20)
	family = models.IntegerField(default=0)
	education = models.IntegerField(default=0)
	friendship = models.IntegerField(default=0)
	health = models.IntegerField(default=0)
	wealth = models.IntegerField(default=0)
	love = models.IntegerField(default=0)

	class Meta:
		ordering = ["name"]
