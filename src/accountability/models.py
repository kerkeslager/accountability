from django.db import models

class Murder(models.Model):
    victim = models.CharField(max_length=64)
    video = models.URLField()

class Murderer(models.Model):
    murder = models.ForeignKey(Murder, on_delete=models.CASCADE, related_name='murderers')
    name = models.CharField(max_length=64)

class Consequence(models.Model):
    murder = models.ForeignKey(Murder, on_delete=models.CASCADE, related_name='consequences')
    text = models.CharField(max_length=256)

