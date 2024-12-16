from django.db import models

from django.contrib.auth.models import User

class TelegramUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField('auth_token', null=True)
    telegram_username = models.TextField('Username', null=True)
    telegram_id = models.PositiveBigIntegerField('TelegramID', null=True)

    def __repr__(self):
        return f'{self.telegram_username or self.telegram_id or self.user}'