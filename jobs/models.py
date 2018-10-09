from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 


class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    job_descripttion = models.CharField(max_length=550)
    create_on = models.DateField()
    closed_on = models.DateField()
    list_per_page = 5
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.job_title

class Job(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
