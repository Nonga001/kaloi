from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # You don't need the role field here anymore
