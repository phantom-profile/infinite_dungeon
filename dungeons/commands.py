from telebot import TeleBot
from telebot.types import Message

from dungeons.services.user_register_service import UserRegisterService
from lib.message_sender import MessageSender


def send_welcome(message: Message, bot: TeleBot):
    ui = MessageSender(bot, message.chat.id)
    result = UserRegisterService(name=message.text, uid=message.from_user.id).call()
    if result.is_fail():
        return ui.send(message=str(result.errors))

    ui.send(message=f'Your adventure starts here, {result.response["user"].name}!')


def message_reply(message: Message, bot: TeleBot):
    ui = MessageSender(bot, message.chat.id)
    ui.send(message=message.text)
