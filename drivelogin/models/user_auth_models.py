from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# class LoginUser(AbstractBaseUser):
#     user_login_name = models.CharField(max_length=254)
#     user_email = models.EmailField(max_length=254, null=False)
#     user_password = models.CharField(max_length=254)
#     user_settings = models.JSONField()

#     AbstractBaseUser.set_password(user_password)

#     USERNAME_FIELD = "user_login_name"
#     EMAIL_FIELD = "user_email"

#     REQUIRED_FIELDS = ["user_email", "user_password"]

#     # class Meta:
#     #     verbose_name = "User"
#     #     verbose_name_plural = "Users"