from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from tauth.app.models import TelegramUserProfile


class TelegramTokenBackend(BaseBackend):
    def authenticate(self, request, token: int = None, telegram_user_id:int = None, telegram_username: str = None):
        # auth by web
        if request:
            request_token = request.COOKIES.get(settings.TG_COOKIES, None)
            if request_token:
                profile = TelegramUserProfile.objects.filter(token=request_token).first()
                if profile:
                    return profile.user
            return None

        # auth by telegram bot
        token_exists = TelegramUserProfile.objects.filter(token=token).first()
        if token_exists:
            return token_exists.user
        else:
            telegram_id_exists = TelegramUserProfile.objects.filter(telegram_id=telegram_user_id).first()
            if telegram_id_exists:
                # user already created, token updating
                telegram_id_exists.token = token
                telegram_id_exists.save()
                return telegram_id_exists.user
            else:
                # new user
                user = User(
                    username=token # why not ? token unique
                )
                user.save()
                TelegramUserProfile.objects.create(
                    user=user,
                    token=token,
                    telegram_username=telegram_username,
                    telegram_id=telegram_user_id
                )
                return user