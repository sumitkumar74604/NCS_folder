from django.db import models


class registration (models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)


def __str__(self):
    return "{0},{1}".format(self.name,self.email)