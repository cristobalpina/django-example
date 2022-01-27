from django.db import models

class Member(models.Model):
    email = models.CharField(max_length=80)