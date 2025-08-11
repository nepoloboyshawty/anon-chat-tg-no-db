from telebot.types import CallbackQuery
from telebot import types

from common import users, sexes, ages, update_user, bot, search_partner
from buttons import user_age_selection, partner_age_selection, partner_gender_selection

@bot.callback_query_handler()
def inline_buttons_handler(call: CallbackQuery):
    user_id = call.from_user.id

    user_gender = users[user_id]['user_gender']
    user_age = users[user_id]['user_age']
    user_like = users[user_id]['like']
    user_dislike = users[user_id]['dislike']
    partner_gender = users[user_id]['partner_gender']
    partner_age = users[user_id]['partner_age']
    last_partner_id = users[user_id]['last_partner_id']

    # Предлагается выбрать свой возраст

    if call.data == "male_gender":
        update_user(user_id, user_gender=sexes[0], user_age=None, like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой мужской пол.\n\nТеперь выберите свой возраст:", reply_markup=user_age_selection)
    
    elif call.data == "female_gender":
        update_user(user_id, user_gender=sexes[1], user_age=None, like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой женский пол.\n\nТеперь выберите свой возраст:", reply_markup=user_age_selection)        

    # Предлагается выбрать пол собеседника

    elif call.data == "user_age_17":        
        update_user(user_id, user_gender=user_gender, user_age=ages[0], like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой возраст до 17 лет.\n\nТеперь выберите пол собеседника:", reply_markup=partner_gender_selection)
    
    elif call.data == "user_age_18_24":
        update_user(user_id, user_gender=user_gender, user_age=ages[1], like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой возраст от 18 до 24 лет.\n\nТеперь выберите пол собеседника:", reply_markup=partner_gender_selection)
    
    elif call.data == "user_age_25_29":
        update_user(user_id, user_gender=user_gender, user_age=ages[2], like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой возраст от 25 до 29 лет.\n\nТеперь выберите пол собеседника:", reply_markup=partner_gender_selection)
    
    elif call.data == "user_age_30_34":
        update_user(user_id, user_gender=user_gender, user_age=ages[3], like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой возраст от 30 до 34 лет.\n\nТеперь выберите пол собеседник:", reply_markup=partner_gender_selection)
    
    elif call.data == "user_age_35":
        update_user(user_id, user_gender=user_gender, user_age=ages[4], like=user_like, dislike=user_dislike, partner_gender=None, partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали свой возраст от 35 лет.\n\nТеперь выберите пол собеседника:", reply_markup=partner_gender_selection)

    # Предлагается выбрать возраст собеседника
    
    elif call.data == "partner_male_gender":        
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, partner_gender=sexes[0], partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали мужской пол собеседника.\n\nТеперь выберите возраст собеседника:", reply_markup=partner_age_selection)
    
    elif call.data == "partner_female_gender":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, partner_gender=sexes[1], partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали женский пол собеседника.\n\nТеперь выберите возраст собеседника:", reply_markup=partner_age_selection)
    
    elif call.data == "partner_any_gender":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, partner_gender=sexes[2], partner_age=None, 
                    partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали любой пол собеседника.\n\nТеперь выберите возраст собеседника:", reply_markup=partner_age_selection)

    # Выбран пол собеседника, далее - его поиск вызовом функции search_partner()

    elif call.data == "partner_age_17":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[0], partner_id=None, last_partner_id=last_partner_id, is_looking=True)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали возраст собеседника до 17 лет.", reply_markup=None)
        search_partner(call)
    
    elif call.data == "partner_age_18_24":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[1], partner_id=None, last_partner_id=last_partner_id, is_looking=True)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали возраст собеседника от 18 до 24 лет.", reply_markup=None)
        search_partner(call)
    
    elif call.data == "partner_age_25_29":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[2], partner_id=None, last_partner_id=last_partner_id, is_looking=True)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали возраст собеседника от 25 до 29 лет.", reply_markup=None)
        search_partner(call)
    
    elif call.data == "partner_age_30_34":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[3], partner_id=None, last_partner_id=last_partner_id, is_looking=True)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали возраст собеседника от 30 до 34 лет.", reply_markup=None)
        search_partner(call)
    
    elif call.data == "partner_age_35":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[4], partner_id=None, last_partner_id=last_partner_id, is_looking=True)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали возраст собеседника от 35 лет.", reply_markup=None)
        search_partner(call)
    
    elif call.data == "partner_age_any":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[5], partner_id=None, last_partner_id=last_partner_id, is_looking=True)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы выбрали любой возраст собеседника.", reply_markup=None)
        search_partner(call)

    # Обработчик мнения пользователей о себе

    elif call.data == "like":
        users[last_partner_id]['like'] += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="Мы рады, что Ваш прошлый собеседник Вам понравился. 🥰", reply_markup=None)
    
    elif call.data == "dislike":
        users[last_partner_id]['dislike'] += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="Очень жаль, что Ваш прошлый собеседник Вам не понравился. 😞", reply_markup=None)
        
    # Обработчик выбора своего пола через настройки
        
    elif call.data == "s_male_gender":
        update_user(user_id, user_gender=sexes[0], user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой пол на мужской.", reply_markup=None)
    
    elif call.data == "s_female_gender":
        update_user(user_id, user_gender=sexes[1], user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой пол на женский.", reply_markup=None)
        
    # Обработчик выбора своего возраста через настройки

    elif call.data == "s_user_age_17":
        update_user(user_id, user_gender=user_gender, user_age=ages[0], like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой возраст до 17 лет.", reply_markup=None)
    
    elif call.data == "s_user_age_18_24":
        update_user(user_id, user_gender=user_gender, user_age=ages[1], like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой возраст от 18 до 24 лет.", reply_markup=None)
    
    elif call.data == "s_user_age_25_29":
        update_user(user_id, user_gender=user_gender, user_age=ages[2], like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой возраст от 25 до 29 лет.", reply_markup=None)
    
    elif call.data == "s_user_age_30_34":
        update_user(user_id, user_gender=user_gender, user_age=ages[3], like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой возраст от 30 до 34 лет.", reply_markup=None)
    
    elif call.data == "s_user_age_35":
        update_user(user_id, user_gender=user_gender, user_age=ages[4], like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили свой возраст от 35 лет.", reply_markup=None)

    # Обработчик выбора пола собеседника через настройки

    elif call.data == "s_partner_male_gender":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=sexes[0], partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили пол собеседника на мужской.", reply_markup=None)
    
    elif call.data == "s_partner_female_gender":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=sexes[1], partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили пол собеседника на женский.", reply_markup=None)
        
    elif call.data == "s_partner_any_gender":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=sexes[2], partner_age=partner_age, partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили пол собеседника на любой.", reply_markup=None)

    # Обработчик выбора возраста собеседника через настройки

    elif call.data == "s_partner_age_17":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[0], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника до 17 лет.", reply_markup=None)
    
    elif call.data == "s_partner_age_18_24":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[1], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника от 18 до 24 лет.", reply_markup=None)
    
    elif call.data == "s_partner_age_25_29":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[2], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника от 25 до 29 лет.", reply_markup=None)
    
    elif call.data == "s_partner_age_30_34":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[3], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника от 30 до 34 лет.", reply_markup=None)
    
    elif call.data == "s_partner_age_35":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[4], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника от 35 лет.", reply_markup=None)
        
    elif call.data == "s_partner_age_any":
        update_user(user_id, user_gender=user_gender, user_age=user_age, like=user_like, dislike=user_dislike, 
                    partner_gender=partner_gender, partner_age=ages[5], partner_id=None, last_partner_id=last_partner_id, is_looking=False)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✅ Вы изменили возраст собеседника на любой.", reply_markup=None)