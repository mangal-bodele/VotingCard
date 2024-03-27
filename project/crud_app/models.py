from django.db import models

class VotingCard(models.Model):
    GENDER=[('M','MALE'),('F','FEMALE'),('O','OTHERS')]
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField( max_length = 20)
    gender = models.CharField(max_length=20,choices=GENDER)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    constituency = models.CharField(max_length=20)
