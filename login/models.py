from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='Email manzil',max_length=250,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    objects=CustomUserManager()
    USERNAME_FIELD='email'

    def __str__(self) -> str:
        return self.email
    
    def has_pern(self,pern,obl=None):
        return self.is_admin
    
    def has_module_perns(self,app_label):
        return self.is_admin