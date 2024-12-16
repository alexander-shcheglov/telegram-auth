# telegram-auth

Modify docker-compose.sample.yml.

Set your values in section:

    environment:
      TELEGRAM_BOT_API_ID: int_your_telegram_api_id
      TELEGRAM_BOT_API_HASH: 'your_telegram_api_hash'
      TELEGRAM_BOT_TOKEN: 'your_telegram_bot_token'

* docker-compose -f docker-compose.sample build
* docker-compose -f docker-compose.sample up

Open http://localhost:8000/