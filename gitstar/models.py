from django.db import models


# Create your models here.
class Stargazer(models.Model):
    login = models.CharField(max_length=60)
    avatar_url = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    html_url = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    blog = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    followers = models.IntegerField()
    following = models.IntegerField()

    def __str__(self):
        return self.login
