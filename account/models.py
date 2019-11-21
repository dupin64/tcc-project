from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, name, user_type, password):
        """
        Creates a user with the given email, first name, last name, user type and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        if not user_type:
            raise ValueError('User must have a user type')

        try:
            user = self.model(
                email=self.normalize_email(email),
                name=name,
                user_type=user_type
            )

            user.set_password(password)
            user.save(using=self._db)

            return {'success': True, 'user': user}
        except:
            return {'success': False}

    def create_superuser(self, email, name, password):
        """
        Creates a superuser with the given email, first name, last name and password.
        """
        user = self.create_user(
            email,
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, null=False)
    user_type = models.CharField(max_length=255, default='patient',
                                 choices=[('patient', 'Patient'), ('specialist', 'Specialist')])

    email = models.EmailField(unique=True, max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Specialist(models.Model):
    title = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
