import telebot

from common import bot, users, settings_messages, update_user

from telebot.types import Message, CallbackQuery
from telebot import types

from handlers import inline_buttons_handler
from buttons import (gender_selection, s_user_gender_selection, s_user_age_selection, s_partner_gender_selection, 
                     s_partner_age_selection, buttons_editing)

def is_registered(user_id):
    """
    Функция проверяет, зарегистрирован ли 
    пользователь или нет.

    :param user_id: уникальный идентификатор 
    пользователя.
    """
    for user, user_params in list(users.items()):

        user_gender = user_params['user_gender']
        user_age = user_params['user_age']
        user_partner_gender = user_params['partner_gender']
        user_partner_age = user_params['partner_age']

        if user == user_id and user_gender is not None and user_age is not None and user_partner_gender is not None \
           and user_partner_age is not None:        
            return True
        
    return False


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    user_id = message.from_user.id

    if is_registered(user_id):        
        bot.send_message(message.chat.id, f"Рады снова Вас видеть! 👋🏻\n\nЧтобы начать поиск, измените параметры, \
                                            введя команду /restart или введите команду /next, чтобы продолжить поиск без изменений.")
        return

    users[user_id] = {"user_gender": None, "user_age": None, "like": 0, "dislike": 0,
                      "partner_gender": None, "partner_age": None, "partner_id": None, "last_partner_id": None, 
                      "is_looking": False}
    
    bot.send_message(message.chat.id, f"Приветствуем Вас в анонимном чат-боте TwoChat! 👋🏻 \
                                            \n\nДля начала Вам стоит выбрать Ваш пол:", reply_markup=gender_selection)


@bot.message_handler(commands=['stop'])
def end_conversation(message: Message):
    try:
        user_id = message.from_user.id
        partner_id = users[user_id]['partner_id']
        
        user_gender = users[user_id]['user_gender']
        user_age = users[user_id]['user_age']
        user_like = users[user_id]['like']
        user_dislike = users[user_id]['dislike']
        user_partner_gender = users[user_id]['partner_gender']
        user_partner_age = users[user_id]['partner_age']
    
        if users[user_id]['is_looking'] == True:

            bot.send_message(user_id, "✅ Вы завершили поиск собеседника. Чтобы продолжить поиск, введите команду /next, \
                                    а для редактирования настроек - /settings.")

            update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                        partner_gender=user_partner_gender, partner_age=user_partner_age, partner_id=None, last_partner_id=None, is_looking=False)
        
        elif partner_id is not None:

            partner_gender = users[partner_id]['user_gender']
            partner_age = users[partner_id]['user_age']
            partner_like = users[partner_id]['like']
            partner_dislike = users[partner_id]['dislike']
            partner_partner_gender = users[partner_id]['partner_gender']
            partner_partner_age = users[partner_id]['partner_age']

            user_opinion = types.InlineKeyboardMarkup()
            user_opinion_like = types.InlineKeyboardButton(f"❤️ {partner_like}", callback_data="like")
            user_opinion_dislike = types.InlineKeyboardButton(f"👎 {partner_dislike}", callback_data="dislike")
            user_opinion.add(user_opinion_like, user_opinion_dislike)

            bot.send_message(user_id, "✅ Вы завершили разговор. Чтобы продолжить поиск, введите команду /next.")
            bot.send_message(user_id, "Пожалуйста, оставьте мнение о собеседнике.", reply_markup=user_opinion)

            partner_opinion = types.InlineKeyboardMarkup()
            partner_opinion_like = types.InlineKeyboardButton(f"❤️ {user_like}", callback_data="like")
            partner_opinion_dislike = types.InlineKeyboardButton(f"👎 {user_dislike}", callback_data="dislike")
            partner_opinion.add(partner_opinion_like, partner_opinion_dislike)

            bot.send_message(partner_id, "Собеседник завершил чат. Чтобы продолжить поиск, введите команду /next. 😔")
            bot.send_message(partner_id, "Пожалуйста, оставьте мнение о собеседнике.", reply_markup=partner_opinion)

            update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                        partner_gender=user_partner_gender, partner_age=user_partner_age, partner_id=None, 
                        last_partner_id=partner_id, is_looking=False)
        
            update_user(partner_id, user_gender=partner_gender, user_age=partner_age, like=partner_like, dislike=partner_dislike, 
                        partner_gender=partner_partner_gender, partner_age=partner_partner_age, partner_id=None, 
                        last_partner_id=user_id, is_looking=False)
        
        else:
            bot.send_message(user_id, "❌ У вас нет собеседника.")
    except KeyError:
        bot.send_message(user_id, "⚠️ В вашем случае Вам нужно воспользоваться командой /start.")


@bot.message_handler(commands=['settings'])
def edit_settings(message: Message):
    if is_registered(message.from_user.id) == False:
        return bot.send_message(message.from_user.id, "⚠️ В вашем случае Вам нужно воспользоваться командой /start.")

    bot.send_message(message.chat.id, "Вы открыли настройки.", reply_markup=buttons_editing)


@bot.message_handler(commands=['stats'])
def show_statistics(message: Message):
    try:
        user_id = message.from_user.id

        user_gender = users[user_id]['user_gender']
        user_age = users[user_id]['user_age']
        user_like = users[user_id]['like']
        user_dislike = users[user_id]['dislike']
        user_partner_gender = users[user_id]['partner_gender']
        user_partner_age = users[user_id]['partner_age']

        bot.send_message(user_id, f"Твой пол: {user_gender}\nТвой возраст: {user_age}\nКол-во лайков: {user_like}\nКол-во дизлайков: {user_dislike}\nПол партнера: {user_partner_gender}\nВозраст партнера: {user_partner_age}")
    except KeyError:
        bot.send_message(user_id, "⚠️ В вашем случае Вам нужно воспользоваться командой /start.")


@bot.message_handler(content_types=['text', 'voice', 'photo', 'video', 'video_note', 'sticker', 'animation'])
def send_message_partner(message: Message):
    try:
        user_id = message.from_user.id
        partner_id = users[user_id]['partner_id']

        if (message.text == settings_messages[0] or message.text == settings_messages[1] 
                or message.text == settings_messages[2] or message.text == settings_messages[3]):
            if partner_id is not None:
                bot.send_message(user_id, "❌ Вы не можете воспользоваться командой во время общения.")
                return

            button_handler(message)
            return

        if partner_id is not None:
            if message.text:
                bot.send_message(partner_id, message.text)
            elif message.voice:
                bot.send_voice(partner_id, message.voice.file_id)
            elif message.photo:
                bot.send_photo(partner_id, message.photo[-1].file_id, caption=message.caption)
            elif message.video:
                bot.send_video(partner_id, message.video.file_id, caption=message.caption)
            elif message.video_note:
                bot.send_video_note(partner_id, message.video_note.file_id)
            elif message.sticker:
                bot.send_sticker(partner_id, message.sticker.file_id)
            elif message.animation:
                bot.send_animation(partner_id, message.animation.file_id)
        else:
            bot.send_message(user_id, "❌ У вас нет собеседника.")
    except KeyError:
        bot.send_message(user_id, "⚠️ В вашем случае Вам нужно воспользоваться командой /start.")


@bot.message_handler(content_types=['text'])
def button_handler(message: Message):
    if message.text == settings_messages[0]:
        bot.send_message(message.chat.id, "Выберите Ваш новый пол:", reply_markup=s_user_gender_selection)
    elif message.text == settings_messages[1]:
        bot.send_message(message.chat.id, "Выберите Ваш новый возраст:", reply_markup=s_user_age_selection)
    elif message.text == settings_messages[2]:
        bot.send_message(message.chat.id, "Выберите новый пол собеседника:", reply_markup=s_partner_gender_selection)
    elif message.text == settings_messages[3]:
        bot.send_message(message.chat.id, "Выберите новый возраст собеседника:", reply_markup=s_partner_age_selection)


bot.callback_query_handler()(inline_buttons_handler)

bot.infinity_polling()