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
