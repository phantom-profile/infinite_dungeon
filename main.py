from os import getenv

from telebot import TeleBot

import launcher.initialize  # noqa
from dungeons.commands import message_reply, send_welcome


def run():
    bot = TeleBot(getenv('TG_BOT_TOKEN'), parse_mode=None)
    bot.register_message_handler(send_welcome, commands=['start'], pass_bot=True)
    bot.register_message_handler(message_reply, pass_bot=True)
    bot.infinity_polling()


if __name__ == '__main__':
    run()
