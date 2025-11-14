from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Roles(models.TextChoices):
    CLIENT = "client", "Клиент"
    COURIER = "courier", "Курьер"
    ADMIN = "admin", "Администратор"

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True")
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=12, choices=Roles.choices, default=Roles.CLIENT)
    phone = models.CharField(max_length=20, blank=True)
    default_address = models.CharField(max_length=255, blank=True)
    entrance = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=50, blank=True)
    intercom = models.CharField(max_length=50, blank=True)
    iin = models.CharField(max_length=12, blank=True)
    avatar_url = models.URLField(blank=True)
    rating = models.FloatField(default=5.0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    email_verified = models.BooleanField(default=False)
    working_districts = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # username не нужен

    objects = UserManager()  # 👈 ВАЖНО — подключаем новый менеджер

    def __str__(self):
        return f"{self.email} ({self.role})"
