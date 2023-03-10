from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PassHolder(models.Model):
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='pass_holder',
    )
    photo = models.ImageField(  # поле для фото
        upload_to='passes/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.person.username


class Pass(models.Model):
    pass_holder = models.ForeignKey(
        PassHolder,
        on_delete=models.CASCADE,
        related_name='passes',
    )
    mfuid = models.CharField(max_length=20)
    valid_from = models.DateTimeField('Действителен с')
    valid_until = models.DateTimeField('Действителен до')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
