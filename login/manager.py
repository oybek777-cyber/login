from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,  email=None, password=None, **extra_fields):


        if not email:
            raise ValueError[' Faoydalanuvchi uchun email talab qilinadi ']
        

        user=self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user



    def create_superuser(self, username, email=None, password=None, **extra_fields):

        user=self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.save(using=self._db)



        return user