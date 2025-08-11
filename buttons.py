from telebot import types

from common import sexes, ages

gender_selection = types.InlineKeyboardMarkup() # Выбор своего пола
male_gender = types.InlineKeyboardButton(sexes[0], callback_data="male_gender")
female_gender = types.InlineKeyboardButton(sexes[1], callback_data="female_gender")
gender_selection.add(male_gender, female_gender)

user_age_selection = types.InlineKeyboardMarkup() # Выбор своего возраста
user_age_17 = types.InlineKeyboardButton(ages[0], callback_data="user_age_17")
user_age_18_24 = types.InlineKeyboardButton(ages[1], callback_data="user_age_18_24")
user_age_25_29 = types.InlineKeyboardButton(ages[2], callback_data="user_age_25_29")
user_age_30_34 = types.InlineKeyboardButton(ages[3], callback_data="user_age_30_34")
user_age_35 = types.InlineKeyboardButton(ages[4], callback_data="user_age_35")
user_age_selection.add(user_age_17, user_age_18_24, user_age_25_29, user_age_30_34, user_age_35)

partner_gender_selection = types.InlineKeyboardMarkup() # Выбор пола собеседника
partner_male_gender = types.InlineKeyboardButton(sexes[0], callback_data="partner_male_gender")
partner_female_gender = types.InlineKeyboardButton(sexes[1], callback_data="partner_female_gender")
partner_any_gender = types.InlineKeyboardButton(sexes[2], callback_data="partner_any_gender")
partner_gender_selection.add(partner_male_gender, partner_female_gender, partner_any_gender)

partner_age_selection = types.InlineKeyboardMarkup() # Выбор возраста собеседника
partner_age_17 = types.InlineKeyboardButton(ages[0], callback_data="partner_age_17")
partner_age_18_24 = types.InlineKeyboardButton(ages[1], callback_data="partner_age_18_24")
partner_age_25_29 = types.InlineKeyboardButton(ages[2], callback_data="partner_age_25_29")
partner_age_30_34 = types.InlineKeyboardButton(ages[3], callback_data="partner_age_30_34")
partner_age_35 = types.InlineKeyboardButton(ages[4], callback_data="partner_age_35")
partner_age_any = types.InlineKeyboardButton(ages[5], callback_data="partner_age_any")
partner_age_selection.add(partner_age_17, partner_age_18_24, partner_age_25_29, partner_age_30_34, partner_age_35, partner_age_any)


buttons_editing = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False) # Меню настроек
editing_gender = types.KeyboardButton("Сменить свой пол")
editing_age = types.KeyboardButton("Сменить свой возраст")
editing_partner_gender = types.KeyboardButton("Сменить пол собеседника")
editing_partner_age = types.KeyboardButton("Сменить возраст собеседника")
buttons_editing.add(editing_gender, editing_age, editing_partner_gender, editing_partner_age)


s_user_gender_selection = types.InlineKeyboardMarkup() # Выбор своего пола через настройки
s_user_male_gender = types.InlineKeyboardButton(sexes[0], callback_data="s_male_gender")
s_user_female_gender = types.InlineKeyboardButton(sexes[1], callback_data="s_female_gender")
s_user_gender_selection.add(s_user_male_gender, s_user_female_gender)

s_user_age_selection = types.InlineKeyboardMarkup() # Выбор своего возраста через настройки
s_user_age_17 = types.InlineKeyboardButton(ages[0], callback_data="s_user_age_17")
s_user_age_18_24 = types.InlineKeyboardButton(ages[1], callback_data="s_user_age_18_24")
s_user_age_25_29 = types.InlineKeyboardButton(ages[2], callback_data="s_user_age_25_29")
s_user_age_30_34 = types.InlineKeyboardButton(ages[3], callback_data="s_user_age_30_34")
s_user_age_35 = types.InlineKeyboardButton(ages[4], callback_data="s_user_age_35")
s_user_age_selection.add(s_user_age_17, s_user_age_18_24, s_user_age_25_29, s_user_age_30_34, s_user_age_35)

s_partner_gender_selection = types.InlineKeyboardMarkup() # Выбор пола собеседника через настройки
s_partner_male_gender = types.InlineKeyboardButton(sexes[0], callback_data="s_partner_male_gender")
s_partner_female_gender = types.InlineKeyboardButton(sexes[1], callback_data="s_partner_female_gender")
s_partner_any_gender = types.InlineKeyboardButton(sexes[2], callback_data="s_partner_any_gender")
s_partner_gender_selection.add(s_partner_male_gender, s_partner_female_gender, s_partner_any_gender)

s_partner_age_selection = types.InlineKeyboardMarkup() # Выбор возраста собеседника через настройки
s_partner_age_17 = types.InlineKeyboardButton(ages[0], callback_data="s_partner_age_17")
s_partner_age_18_24 = types.InlineKeyboardButton(ages[1], callback_data="s_partner_age_18_24")
s_partner_age_25_29 = types.InlineKeyboardButton(ages[2], callback_data="s_partner_age_25_29")
s_partner_age_30_34 = types.InlineKeyboardButton(ages[3], callback_data="s_partner_age_30_34")
s_partner_age_35 = types.InlineKeyboardButton(ages[4], callback_data="s_partner_age_35")
s_partner_age_any = types.InlineKeyboardButton(ages[5], callback_data="s_partner_age_any")
s_partner_age_selection.add(s_partner_age_17, s_partner_age_18_24, s_partner_age_25_29, s_partner_age_30_34, s_partner_age_35, s_partner_age_any)