from django.db import models
from mercury.apps import MercuryConfig

class UserToken(models.Model):

    token = models.CharField(max_length=225, primary_key=True)
    user_id = models.CharField(max_length=500, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.token

    class Meta:
        app_label = MercuryConfig.name
        db_table = "user_token"
        verbose_name = "user_token"
        verbose_name_plural = "user_token"