from django.contrib.auth.models import BaseUserManager

class FlxfittUserManager(BaseUserManager):

    def create_user(self, email, gender, date_of_birth, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
                    raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, gender, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            gender=gender,
            date_of_birth=date_of_birth,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user