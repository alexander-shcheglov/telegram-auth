import uuid

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.utils.deprecation import MiddlewareMixin


class TelegramAuthSessionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.COOKIES.setdefault(settings.TG_COOKIES, str(uuid.uuid4()))
        if request.user.is_anonymous:
            user = authenticate(request=request)
            if user:
                login(request, user)

    def process_response(self, request, response):
        key_value = request.COOKIES.get(settings.TG_COOKIES, None)
        if not key_value:
            key_value = uuid.uuid4()
        response.set_cookie(
            settings.TG_COOKIES,
            key_value
        )
        return response