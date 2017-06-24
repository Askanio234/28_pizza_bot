import os
import telebot
from jinja2 import Template
from models import db_session, Meal


TOKEN = os.getenv('token')
if not TOKEN:
    raise Exception('token should be specified as env variable')


bot = telebot.TeleBot(TOKEN)


with open('templates/catalog.md', 'r', encoding='utf-8') as catalog_file:
    catalog_template = Template(catalog_file.read())


with open('templates/greetings.md', 'r', encoding='utf-8') as greetings_file:
    greetings_template = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_template.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    catalog = db_session.query(Meal).all()
    bot.send_message(message.chat.id,
            catalog_template.render(catalog=catalog), parse_mode='Markdown')


if __name__ == '__main__':
    bot.polling(none_stop=True)
