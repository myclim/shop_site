from django.db import models
from django.contrib.auth.models import AbstractUser



class UsersModel(AbstractUser):
    image = models.ImageField(upload_to='user/images/', blank=True, null=True, verbose_name='Изображениея')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    
    