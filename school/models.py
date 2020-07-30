from django.db import models
from django.conf import settings


# Create your models here.


class Reg(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

	#hackathon
	hack1 = models.CharField('Student', blank=False, null=True,max_length=30)
	hack2 = models.CharField('Student', blank=False, null=True,max_length=30)
	hack3 = models.CharField('Student', blank=False, null=True,max_length=30)
	hack4 = models.CharField('Student', blank=False, null=True,max_length=30)

	#quiz
	quiz1 = models.CharField('Student', blank=False, null=True,max_length=30)
	quiz2= models.CharField('Student', blank=False, null=True,max_length=30)

	#crossword
	cross1= models.CharField('Student', blank=False, null=True,max_length=30)
	cross2= models.CharField('Student', blank=False, null=True,max_length=30)

	#Programming
	prog1= models.CharField('Student', blank=False, null=True,max_length=30)
	prog2= models.CharField('Student', blank=False, null=True,max_length=30)
	prog3= models.CharField('Student', blank=False, null=True,max_length=30)

	#Hardware
	hard1= models.CharField('Student', blank=False, null=True,max_length=30)
	hard2= models.CharField('Student', blank=False, null=True,max_length=30)

	#surprise
	surp1= models.CharField('Student', blank=False, null=True,max_length=30)
	surp2= models.CharField('Student', blank=False, null=True,max_length=30)





