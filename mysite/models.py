from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField("Фото профиля", upload_to="userimages/", default="userimages/default.png")
    is_teacher = models.BooleanField("Учитель?", default=False)


# Модель ответа на задание
class Solution(models.Model):
    code = models.TextField("Код")
    

# Модель дисциплины
# class Discipline(models.Model):
#     title = models.CharField("Название дисциплины", max_length=100)


# Модель курса
# class Course(models.Model):
    