from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    date_registration = models.DateTimeField(auto_now_add=True, verbose_name="Date and Time user registration")

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.username
