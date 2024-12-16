import logging

from asgiref.sync import sync_to_async
from django.core.management import BaseCommand
from django.conf import settings

from telethon import TelegramClient, events
from tauth.app.backends import TelegramTokenBackend

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'run telegram auth bot'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TelegramClient(
            'anon',
            settings.TELEGRAM_BOT_API_ID,
            settings.TELEGRAM_BOT_API_HASH
        ).start(bot_token=settings.TELEGRAM_BOT_TOKEN)
        self.init_bot()

    def init_bot(self):
        self.client.add_event_handler(self.welcome, event=events.NewMessage(pattern='/start [0-9a-f\\-]*'))

    def handle(self, *args, **options):
        self.client.run_until_disconnected()

    async def welcome(self, event):
        token = event.message.text.lstrip('/start ')
        backend = TelegramTokenBackend()
        await sync_to_async(backend.authenticate)(
            request=None,
            token=token,
            telegram_username=event.sender.username,
            telegram_user_id=event.sender.id
        )
