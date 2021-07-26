# Dirección de la api para el chat del bot creado en Telegram a usar.
REQUEST_HEADER = 'https://api.telegram.org/bot[TELEGRAM_TOKEN]'
# Webhook desde el que se despliega el bot.
LOCAL_WEBHOOK_ENDPOINT = '[URL pública del servicio web]/telegram'


# HTTP Request para establecer el webhook y conjugar el chat de telegram con el bot de python
TELEGRAM_INIT_WEBHOOK_URL = REQUEST_HEADER + '/setWebhook?url=' + LOCAL_WEBHOOK_ENDPOINT

# HTTP Request para el envío de mensajes al chat
TELEGRAM_SEND_MESSAGE_URL = REQUEST_HEADER + '/sendMessage?chat_id={}&text={}'