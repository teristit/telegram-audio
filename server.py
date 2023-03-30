import requests
import telebot
import time

from settings import TG_TOKEN

token = TG_TOKEN
bot = telebot.TeleBot(token)
n = True


@bot.message_handler(content_types=['voice'])
def repeat_all_message(message):
    from playsound import playsound
    global n
    try:
        file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

        with open('voice.mp3', 'wb') as f:
            f.write(file.content)

        playsound(file.content)
        n = False
        bot.reply_to(message, 'Сообщение доставлено')
    except Exception:
        bot.reply_to(message, 'Ошибка')


while True:
    bot.polling(none_stop=n)
    n = True
