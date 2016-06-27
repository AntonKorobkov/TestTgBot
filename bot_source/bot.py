import telebot
import json
from weekend_grabber import WeekendMain

__author__ = 'Anton Korobkov'

# Load auth data, create bot
configs = json.load(open('configs.json'))
bot = telebot.TeleBot(configs['auth_token'])

weekend = WeekendMain()


def send_multiple_messages(message, messages):
    """
    To reduce the amount of boilerplate
    :param message:
    :param messages:
    :return:
    """
    for url in messages:
        bot.send_message(message.chat.id, ''.join([messages[url], '\n\n', url]))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    helpmsg = 'Hi! This bot has following commands:\n' \
              '"/hot". Use it to fetch the most fresh stuff\n' \
              '"/top". Use it to fetch the most interesting stuff'
    bot.send_message(message.chat.id, helpmsg)


@bot.message_handler(commands=['hot'])
def get_hot(message):
    link_message = weekend.fetch_hot('b-big-article__title')
    send_multiple_messages(message, link_message)


@bot.message_handler(commands=['top'])
def get_top(message):
    link_message = weekend.fetch_hot('b-top__item__author')
    send_multiple_messages(message, link_message)


@bot.message_handler(content_types=["text"])
def message_handler(message):
    bot.send_message(message.chat.id, 'For now talking is not available')


if __name__ == '__main__':
    bot.polling(none_stop=True)

