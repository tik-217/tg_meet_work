from telebot import types, TeleBot
import os
from dotenv import load_dotenv

load_dotenv()

bot = TeleBot(os.getenv("TG_TOKEN"), parse_mode="HTML")

user_vacancy = ""


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "<b>Вас приветствует бот канала Vacanty. Чтобы разместить вакансию, введите ее содержание.</b>",
    )

    bot.send_message(
        message.chat.id,
        """
Шаблон грамотной вакансии:
	<blockquote> <b>Старший разработчик</b>
	От 300 000 ₽ до вычета налогов
 
	<b>Обязанности:</b>
	• Разработка web-сайтов и мобильных приложений
	• ...

	<b>Требования:</b>
	• Опыт frontend-разработки от 2х лет
	• ...

	<b>Мы предлагаем:</b>
	• Стабильную "белую" конкурентную заработную плату: оклад + премия
	• Расширенную медстраховку
	• ...

	<b>Контакты:</b>
	+78291283843
	t.v.myemail@gmail.com

 	</blockquote>
    	""",
    )

    # btnAddVacancy = types.InlineKeyboardButton("Разместить вакансии", callback_data="add_vacancy")

    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(btnAddVacancy)

    # res = bot.send_message(message.chat.id, "Чтобы разместить вакансии, нажмите кнопку ниже", reply_markup=keyboard)


@bot.message_handler(
    content_types="text",
)
def handler(message: types.Message):
    global user_vacancy

    if len(user_vacancy) == 0:
        bot.send_message(
            message.chat.id, "Спасибо, в ближайшее время, вакансия появится в канале"
        )

        user_vacancy = message.text
    else:
        bot.send_message(
            message.chat.id,
            "Такой команды нет. Пожалуйста, воспользуйтесь доступными командами /start",
        )


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, "Привет, помочь?")


bot.infinity_polling()
