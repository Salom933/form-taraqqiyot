from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = PhoneNumberField()

    def __str__(self):
        return f'{self.name} {self.phonenumber}'