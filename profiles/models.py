from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(
        "Profile picture", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
    )

    #teacher
    t1 = models.CharField('Name', blank=True, null=True,max_length=30)
    t2 = models.CharField('Contact No.', blank=True, null=True,max_length=30)
    t3 = models.CharField('Email Id', blank=True, null=True,max_length=30)

    #Student
    s1 = models.CharField('Name', blank=True, null=True,max_length=30)
    s2 = models.CharField('Contact No.', blank=True, null=True,max_length=30)
    s3 = models.CharField('Email Id', blank=True, null=True,max_length=30)
    
    #hackathon
    hack1 = models.CharField('Participant', blank=True, null=True,max_length=30)
    hack2 = models.CharField('Participant', blank=True, null=True,max_length=30)
    hack3 = models.CharField('Participant', blank=True, null=True,max_length=30)

    #quiz
    quiz1 = models.CharField('Team 1', blank=True, null=True,max_length=30)
    quiz2= models.CharField('Team 2', blank=True, null=True,max_length=30)
    

    #crossword
    cross1= models.CharField('Team 1', blank=True, null=True,max_length=30)
    cross2= models.CharField('Team 1', blank=True, null=True,max_length=30)
    cross3= models.CharField('Team 2', blank=True, null=True,max_length=30)
    cross4= models.CharField('Team 2', blank=True, null=True,max_length=30)

    #Programming
    prog1= models.CharField('Participant', blank=True, null=True,max_length=30)
    

    #Hardware
    hard1= models.CharField('Team 1', blank=True, null=True,max_length=30)
    hard2= models.CharField('Team 2', blank=True, null=True,max_length=30)

    #surprise
    surp1= models.CharField('Team 1', blank=True, null=True,max_length=30)
    surp2= models.CharField('Team 1', blank=True, null=True,max_length=30)
    surp3= models.CharField('Team 2', blank=True, null=True,max_length=30)
    surp4= models.CharField('Team 2', blank=True, null=True,max_length=30)

    #av
    av1= models.CharField('Team 1', blank=True, null=True,max_length=30)
    av2= models.CharField('Team 2', blank=True, null=True,max_length=30)

    #photgraphy
    photo1= models.CharField('Team 1', blank=True, null=True,max_length=30)
    photo2= models.CharField('Team 1', blank=True, null=True,max_length=30)
    photo3= models.CharField('Team 2', blank=True, null=True,max_length=30)
    photo4= models.CharField('Team 2', blank=True, null=True,max_length=30)


    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile".format(self.user)
