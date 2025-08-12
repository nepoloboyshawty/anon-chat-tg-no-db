import telebot
import os

from telebot.types import Message
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('API_TOKEN'))

users = {}
sexes = ["Мужской", "Женский", "Любой"]
ages = ["До 17 лет", "От 18 до 24 лет", "От 25 до 29 лет", "От 30 до 34 лет", "От 35 лет", "Любой"]
settings_messages = [
    "Сменить свой пол", 
    "Сменить свой возраст", 
    "Сменить пол собеседника", 
    "Сменить возраст собеседника"
    "Просмотреть свою статистику"
]

def update_user(user_id, **kwargs):
    """
    Функция обновляет данные пользователя.

    :param user_id: уникальный идентификатор 
    пользователя.
    :param **kwargs: произвольное количество 
    параметров пользователя.
    """
    users[user_id].update({key: value for key, value in kwargs.items()})


@bot.message_handler(commands=['next'])
def search_partner(message: Message):
    try:
        user_id = message.from_user.id

        user_gender = users[user_id]['user_gender']
        user_age = users[user_id]['user_age']
        user_like = users[user_id]['like']
        user_dislike = users[user_id]['dislike']
        user_partner_gender = users[user_id]['partner_gender']
        user_partner_age = users[user_id]['partner_age']

        if user_gender is not None and user_age is not None and user_partner_gender is not None and user_partner_age is not None:

            partner_id = None

            users[user_id] = {"user_gender": user_gender, "user_age": user_age, "like": user_like, "dislike": user_dislike,
                              "partner_gender": user_partner_gender, "partner_age": user_partner_age, "partner_id": None, "last_partner_id": None, "is_looking": True}

            bot.send_message(user_id, "Чтобы остановить поиск, введите команду /stop. Все ваши настройки сохранятся.\n\nИщем нового собеседника... 🔍")
            
            for partner, partner_params in list(users.items()):
                if partner != user_id and partner_params['is_looking'] == True:

                    partner_gender = partner_params['user_gender']
                    partner_age = partner_params['user_age']
                    partner_partner_gender = partner_params['partner_gender']
                    partner_partner_age = partner_params['partner_age']

                    if partner_partner_gender == user_gender and user_partner_gender == partner_gender \
                       and partner_partner_age == user_age and user_partner_age == partner_age:
                        partner_id = partner
                    elif (partner_partner_gender == "Любой" and user_partner_age == "Любой") \
                         or (partner_partner_age == "Любой" and user_partner_age == "Любой"):
                        partner_id = partner

            if partner_id == None:
                return

            partner_gender = users[partner_id]['user_gender']
            partner_age = users[partner_id]['user_age']
            partner_like = users[partner_id]['like']
            partner_dislike = users[partner_id]['dislike']
            partner_partner_gender = users[partner_id]['partner_gender']
            partner_partner_age = users[partner_id]['partner_age']
                    
            users[user_id] = {"user_gender": user_gender, "user_age": user_age, "like": user_like, "dislike": user_dislike,
                              "partner_gender": user_partner_gender, "partner_age": user_partner_age, "partner_id": partner_id, 
                              "last_partner_id": None, "is_looking": False}
            
            users[partner_id] = {"user_gender": partner_gender, "user_age": partner_age, "like": partner_like, "dislike": partner_dislike,
                                 "partner_gender": partner_partner_gender, "partner_age": partner_partner_age, "partner_id": user_id, 
                                 "last_partner_id": None, "is_looking": False}

            bot.send_message(user_id, "Вы нашли собеседника, общайтесь!")
            bot.send_message(partner_id, "Вы нашли собеседника, общайтесь!")
        else:
            bot.send_message(user_id, "❌ Извините, но Вы не можете продолжить поиск собеседника, \
                                       так как мы не обнаружили у Вас важных параметров. \
                                       Воспользуйтесь командой /start для начала взаимодействия с ботом.")
    except KeyError:
        bot.send_message(user_id, "⚠️ В вашем случае Вам нужно воспользоваться командой /start.")