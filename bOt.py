# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1709938468:AAEEDGYd3NT8YIjUNQ1E23jjbh4tEgLznGU')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Сьогодні - ідеальний день для нових починань.","Оптимальний день для того, щоб зважитися на сміливий вчинок! "," Будьте обережні, сьогодні зірки можуть вплинути на ваше фінансове становище.","Кращий час для того, щоб почати нові стосунки або розібратися зі старими.","Плідний день для того, щоб розібратися з накопиченими справами."]
second = ["Але пам'ятайте, що навіть в цьому випадку потрібно не забувати про","Якщо поїдете за місто, заздалегідь подумайте про","Ті, хто сьогодні націлений виконати безліч справ, повинні пам'ятати про","Якщо у вас занепад сил, зверніть увагу на","Пам'ятайте, що думки матеріальні, а значить вам протягом дня потрібно постійно думати про"]
second_add = ["відносини з друзями і близькими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себе і своє здоров'я, інакше до вечора можливий повний розбрат.","побутові питання - особливо ті, які ви не доробили вчора.","відпочинок, щоб не перетворити себе в загнаного коня в кінці місяця."]
third = ["Злі язики можуть говорити вам протилежне, але сьогодні їх слухати не потрібно.","Знайте, що успіх благоволить тільки наполегливим, тому присвятіть цей день вихованню духу.","Навіть якщо ви не зможете зменшити вплив ретроградного Меркурія, то хоча б доведіть справи до кінця.","Не потрібно боятися одиноких зустрічей - сьогодні той самий час, коли вони означають багато.","Якщо зустрінете незнайомця на шляху - проявіть участь, і тоді ця зустріч пообіцяє вам приємні клопоти."]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привіт":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привіт, зараз я розповім тобі гороскоп на сьогодні.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телець', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнюки', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Діва', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Ваги', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпіон', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козеріг', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолій', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Риби', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Обери свій знак зодіаку', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привіт")
    else:
        bot.send_message(message.from_user.id, "Я тебе не розумію. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
